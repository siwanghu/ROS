#!/usr/bin/env python
#encoding=utf-8

import rospy
import move
import threading
import config
from socket import *
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import actionlib
from actionlib_msgs.msg import *
from geometry_msgs.msg import Pose, Point, Quaternion

run=False
rospy.init_node('Cruise', anonymous=False)
navigator = move.Move()

def Monitor_thread():
	global run
	global navigator
	host="localhost"
	port=9999
	addr=(host,port)

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
			if data == "run":
				run=True
			if data == "stop":
				run=False
				navigator.shutdown()
		tcpClient.close()

threading.Thread(target = Monitor_thread,name="Monitor").start()

while True:
	while(run):
		try:
			place=config.getCruiseEnd()
			position = place[0]
			quaternion = place[1]
			rospy.loginfo("Go to (%s, %s) pose", position['x'], position['y'])
			success = navigator.goto(position, quaternion)
		
			if success:
				rospy.loginfo("reached the desired pose")
			else:
				rospy.loginfo("The base failed to reach the desired pose")

			place=config.getCruiseBegin()
			position = place[0]
			quaternion = place[1]
			rospy.loginfo("Go to (%s, %s) pose", position['x'], position['y'])
			success = navigator.goto(position, quaternion)

			if success:
				rospy.loginfo("Hooray, reached the desired pose")
			else:
				rospy.loginfo("The base failed to reach the desired pose")
	
			rospy.sleep(1)

		except rospy.ROSInterruptException:
			rospy.loginfo("Ctrl-C Quitting")
