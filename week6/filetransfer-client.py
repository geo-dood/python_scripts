#!/usr/bin/env python3

#Author: George Maysack-Schlueter
#Description: This is a script for week 6 of python scripting class. This script is for the Networking sockets lab
#***THIS IS THE FILE TRANSFER CLIENT***

import socket

RHOST = '127.0.0.1'  # The server IP address
RPORT = 5001  # The target port as used by the server

# Letting socket know to communicate with the chat server using IPv4 and TCP
C_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
C_SOCK.connect((RHOST, RPORT))

targetFile = open("transferFile.txt", "rb")
fileTransfer = targetFile.read(4096)

while fileTransfer:
    C_SOCK.send(fileTransfer)
    fileTransfer = targetFile.read(4096)

C_SOCK.close()

print("File transfer complete!")