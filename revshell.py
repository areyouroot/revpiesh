#!/usr/bin/env python3
encoding = 'utf-8'
import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    ack= bytes('Connected by'+ HOST, 'ascii')
    s.sendall(ack)
    s.sendall(b'Hello, world')
    data = s.recv(1024)
    print (data.decode(encoding))