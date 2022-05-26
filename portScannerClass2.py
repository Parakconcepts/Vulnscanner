#!/bin/python3
			#VulscannerScript
import socket			#imports socket library
from IPy import IP	#Imports IPy module

class PortScan():
	banners = []
	open_ports = []
	def __init__(self, target, port_num):
		self.target = target
		self.port_num = port_num 
		
	def scan(self):
		for port in range(1,500):						
    			scan_port(port)

	def check_ip(self):		
		try:
		   IP(self.target)
		   return(self.target)
		except ValueError:
		   return socket.gethostbyname(self.target)
	#def get_banner(self):
	#	return s.recv(1024)	  
	
	def scan_port(self,port):			
		try:
			converted_ip = self.check_ip(target)
			sock = socket.socket()		
			sock.settimeout(0.6)		
			sock.connect((ipaddress, port))
			self.open_ports.append
			try:
				banner = get_banner(sock)
				print('[+] Open port' + str(port) + ':' + str(banner.decode().strip('\n')))
			except:
				print(' [+] Open port' + str(port))
		except:
			pass	
	
 if __name__ == "__main__":
 	targets= input('[+] Enter Multiple Targets/Web Address(es) to scan(split multiple targets): ')	#Accepts Multiple 
 	if ',' in targets:
 		for ip_add in targets.split(','):
			scan(ip_add.strip(' '))
	else:
  	     scan(targets)		


