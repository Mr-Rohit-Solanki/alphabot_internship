#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('task0_topic', String, queue_size = 10)
    rospy.init_node('task0_pub', anonymous = True)
    r = rospy.Rate(1)

    while not rospy.is_shutdown():
        strng = "linked at %s"%rospy.get_time()
        rospy.loginfo(strng)
        pub.publish(strng)
        r.sleep()

if __name__ == '__main__':
    try:
         talker()
    except rospy.ROSInterruptException: pass
