#!/usr/bin/env python3

#Author: George Maysack-Schlueter
#Description: This is a script for week 6 of python scripting class. This script is for the Networking sockets lab
#***THIS IS THE CHAT CLIENT***

import socket

RHOST    = '127.0.0.1' # The target IP address, retrieved by FQDN
RPORT    = 5000 # The target port as used by the server
SND_DATA = '' 
RCV_DATA = ''

C_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
C_SOCK.connect((RHOST, RPORT))

#Put the pattern you want to send here.
C_SOCK.send(bytearray(SND_DATA, "utf-8")) 

RCV_DATA = C_SOCK.recv(1024)
print(RCV_DATA.decode())

C_SOCK.close()