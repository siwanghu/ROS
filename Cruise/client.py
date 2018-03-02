#!/usr/bin/env python
#encoding=utf-8

import sys
from socket import *

host="localhost"
port=9999
addr=(host,port)
com=sys.argv[1]

tcpClient = socket(AF_INET,SOCK_STREAM)
tcpClient.connect(addr)

tcpClient.send(com)
print("send ok!")
tcpClient.close()






