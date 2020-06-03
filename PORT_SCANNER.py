from __future__ import print_function
import socket, subprocess, sys
#python 2 or 3
try:
   raw_input          
except NameError:
   raw_input = input

subprocess.call('clear', shell=True)
def logo():
     print( """
                           ~Writeen By
           ____   ___  ____ _____
          |  _ \ / _ \|  _ \_   _|
          | |_) | | | | |_) || |
          |  __/| |_| |  _ < | |
          |_|    \___/|_| \_\|_|
                                      """)

print('''\t

#####################
[VULNARABLE SCANNER ]
#####################

''')

target_ip = raw_input("\t Enter the IP address of the target :").strip()
port_1 = int(raw_input("\t Enter the first port :\t").strip())
port_2 = int(raw_input("\t Enter the last port :\t").strip())
print("~"*50)
print("\n ...Scanning Target  ", target_ip)
print("~"*50)

try:
  for port in range(port_1, port_2):
    sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)

    result = sock.connect_ex((target_ip, port))
    if result==0:
     print("[*] Found Open Port:\t", port)
     sock.close()
 
except KeyboardInterrupt:
  print("[!]****** Scan stopped by user... ")
  sys.exit()
  
except socket.gaierror:
  print("[!] The target's could not be resolved(IP Error)...")
  sys.exit()
  

except socket.error:
  print("[!] *Target is unreachable...")
  sys.exit()
  

logo()
