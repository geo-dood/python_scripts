#!/usr/bin/env python3

# Author: George Maysack-Schlueter
# Description: This is a script for week 6 of python scripting class. This script is for the Networking sockets lab
# ***THIS IS THE CHAT CLIENT***

import socket

RHOST = '127.0.0.1'  # The server IP address
RPORT = 5001  # The target port as used by the server

# Creating the data sent and data received variables as empty strings, so they can wait for input
RCV_DATA = ""

# Letting socket know to communicate with the chat server using IPv4 and TCP
C_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
C_SOCK.connect((RHOST, RPORT))

while True:
    userInput = input("Please enter a message (type 'exit' to exit): ")
    if userInput == "exit":
        print("Goodbye!")
        C_SOCK.close()
        quit()
        break
    else:
        C_SOCK.send(bytearray(userInput, 'utf8'))
        RCV_DATA = C_SOCK.recv(4096)
        print(f"You said: '{RCV_DATA.decode()}'")
