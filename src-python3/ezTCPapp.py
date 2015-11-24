# Author: Jayden Navarro
# Date: 11/24/2015
#!/usr/bin/python3

from ezTCPlib import TcpP2P

name = input( "Enter your first name: " )
print()
ip = input( "Enter target IP address: " )
print()
cPort = int(input( "Enter target port: " ))
print()
sPort = int(input( "Enter local port: " ))
print()

if len(name) == 0: exit(1)

user = name[0].upper()

tcpP2P = TcpP2P( user, ip, cPort, sPort, 1024, 20 )

tcpP2P.start()
