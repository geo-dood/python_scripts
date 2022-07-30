#!/usr/bin/env python3

# Author: George Maysack-Schlueter
# Description: This is a script for week 6 of python scripting class. This script is for the Networking sockets lab
# ***THIS IS THE CHAT CLIENT***

import socket

RHOST = '127.0.0.1'  # The server IP address
RPORT = 50000  # The target port as used by the server

# Creating the data sent and data received variables as empty strings, so they can wait for input
SND_DATA = ''
RCV_DATA = ""

# Letting socket know to communicate with the chat server using IPv4 and TCP
C_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
C_SOCK.connect((RHOST, RPORT))

C_SOCK.send(bytearray(SND_DATA, 'utf8'))

RCV_DATA = C_SOCK.recv(1024)

print(RCV_DATA.decode())

C_SOCK.close()
