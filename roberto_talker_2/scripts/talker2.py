#!/usr/bin/env python
# license removed for brevity

import rospy
from roberto_talker_2.msg import datos

def publisher():

    pub=rospy.Publisher('chatter_avanzado',datos,queue_size=1000)
    rospy.init_node('publicador_roberto_avanzado',anonymous=True)
    rate=rospy.Rate(1)
    counter=0
    counter_par=0
    counter_impar=1

    msg=datos()
    while not rospy.is_shutdown():
        msg.header.seq=counter
        msg.header.stamp=rospy.Time.now()
        msg.header.frame_id="0"
        mensaje1_str="hello world %d" % counter_par
        mensaje2_str="hello world %d" % counter_impar
        msg.mensaje1=mensaje1_str
        msg.mensaje2=mensaje2_str
        msg.score=10

        #rospy.loginfo("enviado mensaje %d con marca de tiempo %d.%d",msg.header.seq,msg.header.stamp.secs,msg.header.stamp.nsecs)
        rospy.loginfo (msg)
        
        pub.publish(msg)
        rate.sleep()
        counter +=1 
        counter_par +=2
        counter_impar +=2

if __name__ == '__main__':
	
    try:
		publisher()
    except rospy.ROSInterruptException:
        pass
