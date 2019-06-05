#!/usr/local/bin/python3

import socketserver


class TCPHandlerServer(socketserver.BaseRequestHandler):

    def handle(self):

        self.data = self.request.recv(1024).strip()
        print(f'{self.client_address[0]}: {self.client_address[1]}')
        print(self.data)
        self.request.sendall(self.data.upper())


if __name__ == "__main__":
    HOST, PORT = '127.0.0.1', 9999

    with socketserver.TCPServer((HOST, PORT), TCPHandlerServer) as server:
        server.serve_forever()

