#!/usr/bin/env python

from socket import *

HOST = 'localhost'
PORT=21567
BUFSIZ=1024
ADDR=(HOST,PORT)

tcpCliSock = socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data_send=input('input<')
    if not data_send:
        break
    tcpCliSock.send(data_send.encode('utf-8'))
    data_recv=tcpCliSock.recv(BUFSIZ)
    if not data_recv:
        break
    print(data_recv)

tcpCliSock.close()
