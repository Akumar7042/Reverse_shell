#/bin/python
#pip install pygeoip

import dns.resolver as dns
import pygeoip
import dns.resolver
from pexpect import pxssh
import getpass
import csv



domain = raw_input("\n\nEnter domain name\nExample - google.com\n")
while 1:
	print("\n\nChoose One Option \n")
	print("1. Find basic ipv4 Address")
	print("2. Find basic ipv6 Address")
	print("3. Find mail server address")
	print("4. Find State of Authority")
	print("5. Find exact location of given Domain")

	ch = input("\nEnter your choise : ")
	if ch == 1:
		print("IP Address (IPv4) of "+domain+" is")
		answer = dns.resolver.query(domain, "A")
		print answer[0]


	if ch == 2:
		try:
			answer = dns.resolver.query(domain, "AAAA")
			print(" Ipv6 Address of "+domain+" is")
			print answer[0]
		except dns.resolver.NoAnswer:
			print "No AAAA"
		except dns.resolver.NXDOMAIN:
			print "No such domain"
	if ch == 3:
		import dns.resolver
		try:
			for x in dns.resolver.query(domain, 'MX'):
				print(x.to_text())
		except:
			print "Type Error "
	if ch == 4:
		import dns.resolver
		answers = dns.resolver.query(domain, 'SOA')
		print 'query qname:', answers.qname, ' num ans.', len(answers)
		for rdata in answers:
			print('serial: %s  tech: %s' % (rdata.serial, rdata.rname))
    		print('refresh: %s  retry: %s' % (rdata.refresh, rdata.retry))
    		print('expire: %s  minimum: %s' % (rdata.expire, rdata.minimum))
    		print('mname: %s' % (rdata.mname))

   	if ch == 5:
   		try:
			answer = dns.resolver.query(domain, 'A')
			b = str(answer[0])
   			query = pygeoip.GeoIP("GeoLiteCity.dat")
   			result = query.record_by_addr(b)
   			print"City : ",result['city'] 
   			print"Country Code: ",result['country_code']
   			print"Country Name : ",result['country_name']
   			print"Time Zone : ",result['time_zone']
   			print"Metro Code : ",result['metro_code']
   			print"Area Code : ",result['area_code']
   			print"DMA Code : ",result['dma_code']
   			print"Latitude : ",result['latitude']
   			print"Longitude : ",result['longitude']
   			print"Region Code : ", result['region_code']
   		except:
   			print "error found"


