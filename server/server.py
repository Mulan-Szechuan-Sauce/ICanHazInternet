#!/usr/bin/env python3

import cgi
from http.server import BaseHTTPRequestHandler, HTTPServer

HOST = 'localhost'
PORT = 1337

class ICanHasHandle(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
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

        self.wfile.write(bytes('\n'.join(self.getUrls()), 'utf8'))

    def getUrls(self):
        # TODO: Bloom it up.
        return ['bloom it up']

    def siftUrls(self, urls):
        # TODO: Bloom it up.
        for url in urls:
            print(url)

if __name__ == "__main__":
    print('Getting all interwebs!')
    server_address = (HOST, PORT)
    try:
        HTTPServer(server_address, ICanHasHandle).serve_forever()
    except KeyboardInterrupt:
        print('Killing the interwebs :(')
