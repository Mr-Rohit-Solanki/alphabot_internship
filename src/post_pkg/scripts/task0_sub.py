#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(rospy.get_caller_id()+" We are %s ",data.data)

def listener():
    rospy.init_node('task0_sub',
                    anonymous = True)
    rospy.Subscriber("task0_topic", String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
