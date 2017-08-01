#!/usr/bin/env python3

import cgi
import sqlite3
from bloom_filter import BloomFilter
from http.server import BaseHTTPRequestHandler, HTTPServer

HOST = '192.168.0.104'
PORT = 1337
BLOOM = BloomFilter(10000)
URLS_PER_CLIENT = 1
TODO = ['google.com']
DB = sqlite3.connect('icanhasdatabase').cursor()

class ICanHasHandle(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(401)
        self.send_header('Content-type','text/html')
        self.end_headers()

        message = "Get off my damn property!" # them kids...
        self.wfile.write(bytes(message, 'utf8'))

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        if 'content-length' in self.headers:
            content_len = int(self.headers['content-length'])
            body = self.rfile.read(content_len).decode('utf8')
            self.siftUrls(body.splitlines())

        print('Backlog Size: %d' % len(TODO))
        self.wfile.write(bytes('\n'.join(self.getUrls()), 'utf8'))

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


if __name__ == '__main__':
    print('Getting all interwebs!')
    server_address = (HOST, PORT)
    DB.execute('CREATE TABLE IF NOT EXISTS urls (url text primary key)')
    try:
        HTTPServer(server_address, ICanHasHandle).serve_forever()
    except KeyboardInterrupt:
        print('Killing the interwebs :(')
