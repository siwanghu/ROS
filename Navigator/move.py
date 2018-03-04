#!/usr/bin/env python
#encoding=utf-8
#coding: siwanghu

import rospy
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import actionlib
from actionlib_msgs.msg import *
from geometry_msgs.msg import Pose, Point, Quaternion

class Move():
	def __init__(self):
		self.goal_sent = False
		rospy.on_shutdown(self.shutdown)
		self.move_base = actionlib.SimpleActionClient("move_base", MoveBaseAction)
		rospy.loginfo("Wait for the action server to come up")
		self.move_base.wait_for_server(rospy.Duration(5))

	def goto(self, pos, quat):
		self.goal_sent = True
		goal = MoveBaseGoal()
		goal.target_pose.header.frame_id = 'map'
		goal.target_pose.header.stamp = rospy.Time.now()
		goal.target_pose.pose = Pose(Point(pos['x'], pos['y'], 0.000),Quaternion(quat['r1'], quat['r2'], quat['r3'], quat['r4']))
		self.move_base.send_goal(goal)
		success = self.move_base.wait_for_result(rospy.Duration(60))
		state = self.move_base.get_state()
		result = False
		
		if success and state == GoalStatus.SUCCEEDED:
			result = True
		else:
			self.move_base.cancel_goal()

		self.goal_sent = False
		return result
	
	def shutdown(self):
		if self.goal_sent:
			self.move_base.cancel_goal()
		rospy.loginfo("Stop")
		rospy.sleep(1)

