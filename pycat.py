#!/usr/bin/env python3

encoding = 'utf-8'
import socket
import time
print ("this is a no root shell")
choice=int(input("1)start a listener\n2)connect to a shell\nenter ur choice:"))

def pysh():
        cmd=input("PieSh-[]-:")
        
        if (cmd==''):
            pysh()

        cmd= bytes(cmd, 'ascii')
        conn.sendall(cmd)
        data= conn.recv(4024)
        print (data.decode(encoding))
        pysh()

if (choice==1):

    #exe this 
    print("run it")
    HOST = '10.0.2.5'  # The server's hostname or IP address
    PORT = 65432        # The port used by the server

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        s.connect((HOST, PORT))
        ack= bytes('Connected by'+ HOST, 'ascii')
        s.sendall(ack)
    
        while True():

            s.sendall(b'Hello, world')
            data = s.recv(4024)
        print (data.decode(encoding))

else:

    HOST = '10.0.2.5'  # Standard loopback interface address (localhost)
    PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        data = conn.recv(4024)
        print (data.decode(encoding))
        data = b""
        pysh()