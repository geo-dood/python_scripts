#!/usr/bin/env python3

#Author: George Maysack-Schlueter
#Description: This is a script for week 6 of python scripting class. This script is for the Networking sockets lab
#***THIS IS THE CHAT CLIENT***

import socket

headerSize = 10
remoteHost = '127.0.0.1'
remotePort = 60602

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((remoteHost, remotePort))

while True:

    fullMessage = ''
    newMessage = True
    while True:
        receivedMessage = clientSocket.recv(16)
        if newMessage:
            print(f"New Message Length: {receivedMessage[:headerSize]}")
            messageLength = int(receivedMessage[:headerSize])
            newMessage = False

        fullMessage += receivedMessage.decode("utf-8")

        if len(fullMessage)-headerSize == messageLength:
            print("full message received")
            print(fullMessage[headerSize:])
            newMessage = True
            fullMessage = ''
            
        print(fullMessage)