#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64

def rrbot_talker():
    pub = rospy.Publisher('/rrbot/joint1_position_controller/command', Float64, queue_size = 10)
    rospy.init_node('rrbot_talker', anonymous = True)
    rate = rospy.Rate(5) #5hz
    

    while not rospy.is_shutdown():
        joint_control = -1.5
        pub.publish(joint_control)
        rate.sleep

if __name__ == '__main__':
    try:
        rrbot_talker()

    except rospy.ROSInterruptException:
        pass
