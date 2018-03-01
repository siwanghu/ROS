#!/usr/bin/env python
#encoding=utf-8

import rospy
import move
import threading
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
	tcpServer.listen(5)

	while True:
		print("begin listen...........!")
		tcpClient,addr = tcpServer.accept()
		print("connected from:",addr)
	
		while True:
			data=tcpClient.recv(1024)
			if not data:
				break
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
			position = {'x': 2.522, 'y' : 3.768}
			quaternion = {'r1' : 0.000, 'r2' : 0.000, 'r3' : -0.791, 'r4' : 0.612}
			rospy.loginfo("Go to (%s, %s) pose", position['x'], position['y'])
			success = navigator.goto(position, quaternion)
		
			if success:
				rospy.loginfo("reached the desired pose")
			else:
				rospy.loginfo("The base failed to reach the desired pose")


			position = {'x':2.351 , 'y' : -0.442}
			quaternion = {'r1' : 0.000, 'r2' : 0.000, 'r3' : 0.761, 'r4' : 0.648}
			rospy.loginfo("Go to (%s, %s) pose", position['x'], position['y'])
			success = navigator.goto(position, quaternion)

			if success:
				rospy.loginfo("Hooray, reached the desired pose")
			else:
				rospy.loginfo("The base failed to reach the desired pose")
	
			rospy.sleep(1)

		except rospy.ROSInterruptException:
			rospy.loginfo("Ctrl-C Quitting")











































