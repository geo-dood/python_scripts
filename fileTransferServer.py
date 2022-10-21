#!/usr/bin/env python3

# Author: George Maysack-Schlueter
# Description: This is a script for week 6 of python scripting class. This script is for the Networking sockets lab
# ***THIS IS THE FILE TRANSFER SERVER***

import socket

# Local host
LHOST = '127.0.0.1'
LPORT = 5001

# Initializing connection with the chat client using IPv4 and TCP
L_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
L_SOCK.bind((LHOST, LPORT))

L_SOCK.listen(1)

serverFile = open('received.txt', 'wb')
print("\n Copied file name will be 'received.txt' on server-side\n")

while True:
    L_CONN, addr = L_SOCK.accept()

    RCV_DATA = L_CONN.recv(4096)
    while RCV_DATA:
        serverFile.write(RCV_DATA)
        RCV_DATA = L_CONN.recv(4096)

    serverFile.close()
    print("\n File successfully copied! \n")
    # This line sends the data back to the client
    L_CONN.close()
    break
