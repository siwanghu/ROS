#!/usr/bin/env python
#encoding=utf-8
#coding: siwanghu

import tkMessageBox
from Tkinter import *
from socket import *

wait=True
flag=False

def begin():
    global wait
    global flag
    if wait == True and flag == False:
        flag=True
        wait=False
        host="localhost"
        port=9999
        addr=(host,port)
        com="run"
        tcpClient = socket(AF_INET,SOCK_STREAM)
        tcpClient.connect(addr)
        tcpClient.send(com)
        tcpClient.close()

def end():
    global wait
    global flag
    if wait == False and flag == True:    
        flag=False
        wait=True
        host="localhost"
        port=9999
        addr=(host,port)
        com="stop"
        tcpClient = socket(AF_INET,SOCK_STREAM)
        tcpClient.connect(addr)
        tcpClient.send(com)
        tcpClient.close()

def door():
    global wait
    global flag
    if flag == False and wait == True:    
        host="localhost"
        port=10000
        addr=(host,port)
        com="door"
        tcpClient = socket(AF_INET,SOCK_STREAM)
        tcpClient.connect(addr)
        tcpClient.send(com)
        tcpClient.close()

def counter():
    global wait
    global flag
    if flag == False and wait == True:    
        host="localhost"
        port=10000
        addr=(host,port)
        com="counter"
        tcpClient = socket(AF_INET,SOCK_STREAM)
        tcpClient.connect(addr)
        tcpClient.send(com)
        tcpClient.close()
    
def atm():
    global wait
    global flag
    if flag == False and wait == True:    
        host="localhost"
        port=10000
        addr=(host,port)
        com="atm"
        tcpClient = socket(AF_INET,SOCK_STREAM)
        tcpClient.connect(addr)
        tcpClient.send(com)
        tcpClient.close()

window = Tk()
window.title("底盘测试界面")
window.resizable(0, 0)

Button(window, text="开始巡航", fg="blue",bd=5,width=40,height=3,command=begin).pack()

Button(window, text="关闭巡航", fg="blue",bd=5,width=40,height=3,command=end).pack()

Button(window, text="出口", fg="blue",bd=5,width=40,height=3,command=door).pack()

Button(window, text="柜台", fg="blue",bd=5,width=40,height=3,command=counter).pack()

Button(window, text="ATM机", fg="blue",bd=5,width=40,height=3,command=atm).pack()

window.mainloop()