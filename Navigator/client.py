#!/usr/bin/env python
#encoding=utf-8

import sys
from socket import *

host=sys.argv[1]
port=int(sys.argv[2])
addr=(host,port)
com=sys.argv[3]

tcpClient = socket(AF_INET,SOCK_STREAM)
tcpClient.connect(addr)

tcpClient.send(com)
print("send ok!")
tcpClient.close()






