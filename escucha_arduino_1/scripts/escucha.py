#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback(msg):
	rospy.loginfo (msg.data)

def subscriber():
	rospy.init_node(‘suscriptor_de_roberto’,anonymous=True)
	sub=rospy.Subscriber(‘/chatter’,String,callback)
	rospy.spin()

if __name__==’main’:
	try:
		publisher()
	except rospy.ROSInterruptException:
		pass
