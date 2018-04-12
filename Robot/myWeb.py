#!/usr/bin/env python
#encoding=utf-8
#coding: siwanghu
import web  
urls=('/', 'index')  

class index:  
    def GET(self):  
		name=web.input(types=None,ids=None)
		ids=name.ids
		types=name.types
		if types=="crui":
			host="192.168.0.212"
			port=9999
			addr=(host,port)
			com=ids
			tcpClient = socket(AF_INET,SOCK_STREAM)
			tcpClient.connect(addr)
			tcpClient.send(com)
			tcpClient.close()
		if types=="navi":
			host="192.168.0.212"
			port=10000
			addr=(host,port)
			com=ids
			tcpClient = socket(AF_INET,SOCK_STREAM)
			tcpClient.connect(addr)
			tcpClient.send(com)
			tcpClient.close()

app = web.application(urls, globals())  
app.run() 
