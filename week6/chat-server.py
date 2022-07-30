#!/usr/bin/env python3

# Author: George Maysack-Schlueter
# Description: This is a script for week 6 of python scripting class. This script is for the Networking sockets lab
# ***THIS IS THE CHAT SERVER***

import socket

# Local host
LHOST = ''
LPORT = 50000
# Creating received data variable that will be 'listening' for the user input
RCV_DATA = ""

# Initializing connection with the chat client using IPv4 and TCP
L_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
L_SOCK.bind((LHOST, LPORT))

while 1:
    L_SOCK.listen(1)
    L_CONN, addr = L_SOCK.accept()
    print('Connected by', addr)
    RCV_DATA = L_SOCK.recv(1024)
    if not RCV_DATA:
        break
    print(f"The server received the following: {RCV_DATA}")
    # This line sends the data back to the client
    L_SOCK.sendall(RCV_DATA)
L_CONN.close()
