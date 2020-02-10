#!/usr/bin/env python
# license removed for brevity

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
import time
from std_srvs.srv import Empty

x=0
y=0
yaw=0

def posecallback(pose_message):
  global x,y,yaw
  x=pose_message.x
  y=pose_message.y 
  yaw=pose_message.theta


def move(speed,distance,is_forward):
  velocity_message=Twist()
  global x,y

  x0=x
  y0=y
  rospy.loginfo("x %f y %f",x,y)
  if (is_forward):
    velocity_message.linear.x=abs(speed)
  else:
    velocity_message.linear.x=-abs(speed)

  distance_moved=0.0
  loop_rate=rospy.Rate(10)#we publish the velocity at 10Hz
  velocity_publisher=rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=1000)

  while True:
    rospy.loginfo("turtlesim moves....")
    velocity_publisher.publish(velocity_message)
    loop_rate.sleep()
    distance_moved=abs(math.sqrt((x-x0)**2+(y-y0)**2))
    rospy.loginfo ("x %f y %f distance_moved %f",x,y,distance_moved)
    if not (distance_moved<distance):
      rospy.loginfo("distance reached")
      break
  
  #we stop the robot
  velocity_message.linear.x=0
  velocity_publisher.publish(velocity_message)

def rotate(angular_speed_degree,relative_angle_degree,clockwise):
  #by default in ROS all angles are in radians, for angles and angular velocities

  global yaw
  velocity_message = Twist()
  velocity_message.linear.x=0
  velocity_message.linear.y=0
  velocity_message.linear.z=0
  velocity_message.angular.x=0
  velocity_message.angular.y=0
  velocity_message.angular.z=0

  #we get current localization
  theta0=yaw
  
  angular_speed=math.radians(abs(angular_speed_degree))
  if (clockwise):
    velocity_message.angular.z=-abs(angular_speed)
  else:
    velocity_message.angular.z=abs(angular_speed)

  angle_moved=0.0
  loop_rate=rospy.Rate(10)
  velocity_publisher=rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=1000)

  t0=rospy.Time.now().to_sec()

  while True:
    rospy.loginfo("turtlesim rotates....")
    velocity_publisher.publish(velocity_message)
    
    t1=rospy.Time.now().to_sec()
    angle_degree_moved=(t1-t0)*angular_speed_degree
    loop_rate.sleep()

    if (angle_degree_moved>relative_angle_degree):
      rospy.loginfo("angle reached ")
      break

  #finally, stop the robot
  velocity_message.angular.z=0
  velocity_publisher.publish(velocity_message)
    
    
def publisher():

    
    rospy.init_node('turtlesim_roberto',anonymous=True)

    #velocity_publisher=rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=1000)
    #es posible que haya que cambiar el rate...
    #rate=rospy.Rate(10) 
    pose_subscriber=rospy.Subscriber('/turtle1/pose',Pose,posecallback)
    time.sleep(2)
    #el sleep anterior es necesario para que le de tiempo a adquirir algun valor de posicion inicial...
    move(1.0,3.0,True)
    rotate(30,90,False)
    move(1.0,3.0,True)
    rotate(30,90,False)
    move(1.0,3.0,True)
    rotate(30,90,False)
    move(1.0,3.0,True)





    
    

if __name__ == '__main__':
	
    try:
		publisher()
    except rospy.ROSInterruptException:
        pass
