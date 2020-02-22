#!/usr/bin/env python
# license removed for brevity

import rospy
from roberto_talker_2.msg import datos

def callback(data):
    rospy.loginfo("recibido mensaje %d con marca de tiempo %d.%d",data.header.seq,data.header.stamp.secs,data.header.stamp.nsecs)
    rospy.loginfo(data)
    #print 'mensaje 1' + str(msg.mensaje1)
    #print 'mensaje 2' + str(msg.mensaje2)
    #print ' '


def memory_subscriber():

    rospy.init_node('suscriptor_avanzado_roberto',anonymous=True)
    rospy.Subscriber('chatter_avanzado',datos,callback)
    rospy.spin()

if __name__ == "__main__":
  
    memory_subscriber()
    