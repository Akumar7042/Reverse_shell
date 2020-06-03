import sys
try:
    import nmap
except:
    sys.exit("[!] Looks nmap module is missing use: pip install python-nmap")

if len(sys.argv) != 3:
    sys.exit("USAGE:python Nmap.py Target_ip port_number")
addr = str(sys.argv[1])
port = str(sys.argv[2])

my_scanner = nmap.PortScanner()
my_scanner.scan(addr, port)
for host in my_scanner.all_hosts():
    #if not my_scanner[host].hostname():
     #   print("Not able to find the hostname for IP address %s") % (host)
    #else:
        #print("The Hostname for IP address  %s ---> is %s ") % (host, my_scanner[host].hostname())
        print("---------------------------------------")
        print('HostName: %s'% my_scanner[host].hostname())
        print('State : %s' % my_scanner[host].state())
        print('Scan Info: %s'% my_scanner.scaninfo())
        print('-------------------------------------')
        if my_scanner[host].state()=='up':
         for proto in my_scanner[host].all_protocols():
          print('Protocol : %s' % proto)
 
          lport = my_scanner[host][proto].keys()
          lport.sort()
          for port in lport:
             print ('port : %s\tstate : %s' % (port, my_scanner[host][proto][port]['state']))

        else:
             print("Host Is Down")
