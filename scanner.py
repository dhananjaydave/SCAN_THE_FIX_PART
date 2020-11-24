
#!/bin/python3

import sys
import socket
from datetime import datetime

if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1])
else:
	print("Invalid Amount Of Arguement.")
	print("Syntax: python3 scanner.py <ip>")
	sys.exit()	

print("-" * 50)
print("Scanning Target "+target)
print("Time Started:"+str(datetime.now()))
print("-" * 50)	

try:
	for port in range(50,85):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port))
		print("Checking port {}".format(port))
		if result ==0:
			print("Port {} Is Open".format(port))
		s.close()
		
except KeyboardInterrupt:
	print("\nExiting Program.")
	sys.exit()
except socket.gaierror:
	print("Host Could Not Be Resolved")
	sys.exit()
except socket.error:
	print("Cant't connect To Server.")
	sys.exit()	
