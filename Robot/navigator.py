#!/usr/bin/env python
#encoding=utf-8
#coding: siwanghu

import rospy
import move
import threading
import config
import sys
from socket import *
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import actionlib
from actionlib_msgs.msg import *
from geometry_msgs.msg import Pose, Point, Quaternion

run="wait"
rospy.init_node('Navigator', anonymous=False)
navigator = move.Move()

def Monitor_thread():
	global run
	global navigator
	host="192.168.0.212"
	port=10000
	addr=(host,port)

	setdefaulttimeout(sys.maxint)
	tcpServer = socket(AF_INET,SOCK_STREAM)
	tcpServer.bind(addr)
	tcpServer.listen(10)

	while True:
		print("begin listen...........!")
		tcpClient,addr = tcpServer.accept()
		print("connected from:",addr)
		
		data=tcpClient.recv(1024)
		if not data:
			tcpClient.close()
			continue
		else:
			run=data
		tcpClient.close()

threading.Thread(target = Monitor_thread,name="Monitor").start()
places=config.getPlaces()

while True:
	try:
		if run == "wait":
			continue
		else:
			for key in places.keys():
				if run == key:
					run = "wait"
					position = places[key][0]
					quaternion = places[key][1]
					rospy.loginfo("Go to (%s, %s) pose", position['x'], position['y'])
					success = navigator.goto(position, quaternion)
					if success:
						rospy.loginfo("reached the desired pose")
					else:
						rospy.loginfo("The base failed to reach the desired pose")
					break
	except rospy.ROSInterruptException:
		rospy.loginfo("Ctrl-C Quitting")