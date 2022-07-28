#!/usr/bin/env python3

#Author: George Maysack-Schlueter
#Description: This is a script for week 6 of python scripting class. This script is for the Networking sockets lab
#***THIS IS THE CHAT SERVER***

import socket
import time

headerSize = 10
localHost = '127.0.0.1'
localPort = 60602

serverStream = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverStream.bind((localHost, localPort))
serverStream.listen(5)

while True:
    clientsocket, address = serverStream.accept()
    print(f'Connection from {address} has been established')

    banner = "Please Enter a Message!"
    banner = f'{len(banner):<{headerSize}}' + banner

    clientsocket.send(bytes(banner, "utf-8"))

    while True:
        time.sleep(3)
        banner = "Please Enter a Message!"
        banner = f'{len(banner):<{headerSize}}' + banner
        clientsocket.send(bytes(banner, "utf-8"))
