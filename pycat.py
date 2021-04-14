#!/usr/bin/env python3
encoding = 'utf-8'
import socket
choice=int(input("1)start a listener\n2)connect to a shell\nenter ur choice:"))
if (choice==1):
    #exe this 
    print("run it")
else:
    HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
    PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        data = conn.recv(1024)
        print (data.decode(encoding))
        while True:
            conn.sendall(b'Hello, world')
            data = conn.recv(1024)
            print (data.decode(encoding))
            conn.sendall(data)
            exit()