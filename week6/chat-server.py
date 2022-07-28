#!/usr/bin/env python3

#Author: George Maysack-Schlueter
#Description: This is a script for week 6 of python scripting class. This script is for the Networking sockets lab
#***THIS IS THE CHAT SERVER***

import socket

headerSize = 20

# Empty quotes means listen on all available interfaces
localHost = '127.0.0.1'
# Arbitrary non-privileged port to listen on             	
localPort = 1234
RCV_DATA = ""         	

serverStream = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverStream.bind((localHost, localPort))
serverStream.listen(5)

while True:
    clientsocket, address = serverStream.accept()
    print(f'Connection from {address} has been established')

    message = "Welcome to the Chat Room!"
    message = f'{len(message):<{headerSize}]}' + message

    clientsocket.send(bytes(message, "utf-8"))
    clientsocket.close()
