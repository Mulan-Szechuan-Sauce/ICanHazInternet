#!/usr/bin/env python3

import argparse
import cgi
import json
import sqlite3

from bloom_filter import BloomFilter
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse

BLOOM = BloomFilter(10000)
URLS_PER_CLIENT = 1
TODO = ['google.com']
DB = sqlite3.connect('icanhazdatabase').cursor()

class ICanHasHandle(BaseHTTPRequestHandler):
    def do_GET(self):
        parsedURL = urlparse(self.path)

        if parsedURL.path == '/admin':
            # Such amazing security right?
            self.sendSuccess()
            with open('admin.htm') as f:
                self.wfile.write(bytes(f.read(), 'utf8'))
        elif parsedURL.path == '/admin/info':
            self.sendSuccess()
            info = {
                    'todo': TODO,
                    }
            self.wfile.write(bytes(json.dumps(info), 'utf8'))
        else:
            self.send404()

    def do_POST(self):
        parsedURL = urlparse(self.path)

        if parsedURL.path == '/':
            self.sendSuccess()

            if 'content-length' in self.headers:
                content_len = int(self.headers['content-length'])
                body = self.rfile.read(content_len).decode('utf8')
                self.siftUrls(body.splitlines())

            print('Backlog Size: %d' % len(TODO))
            self.wfile.write(bytes('\n'.join(self.getUrls()), 'utf8'))
        elif parsedURL.path == '/blacklistdomain':
            self.sendSuccess()
            self.blacklist(parsedURL.query)
            self.wfile.write(bytes('blacklisted', 'utf8'))
        else:
            self.send404()

    def sendSuccess(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

    def send404(self):
        self.send_response(404)
        self.send_header('Content-type','text/html')
        self.end_headers()

        message = "Get off my damn property!" # them kids...
        self.wfile.write(bytes(message, 'utf8'))

    def getUrls(self):
        urls = TODO[:URLS_PER_CLIENT]
        del TODO[:URLS_PER_CLIENT]
        return urls

    def siftUrls(self, urls):
        for url in urls:
            if url in BLOOM:
                DB.execute('SELECT * FROM urls WHERE url=?', [url])
                if DB.fetchall == []:
                    DB.execute('INSERT INTO urls (url) VALUES (?)', [url])
                    BLOOM.add(url)
                    TODO.append(url)
            else:
                DB.execute('INSERT INTO urls (url) VALUES (?)', [url])
                BLOOM.add(url)
                TODO.append(url)

    def blacklist(self):
        # TODO
        pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', dest='host', type=str, default='localhost')
    parser.add_argument('--port', dest='port', type=int, default=1337)
    args = parser.parse_args()

    print('Getting all interwebs!')
    server_address = (args.host, args.port)
    DB.execute('CREATE TABLE IF NOT EXISTS urls (url text primary key)')
    try:
        HTTPServer(server_address, ICanHasHandle).serve_forever()
    except KeyboardInterrupt:
        print('Killing the interwebs :(')
