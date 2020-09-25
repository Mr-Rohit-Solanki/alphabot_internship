#!/usr/bin/env python

import rospy
#import roslib
#import tf
from geometry_msgs.msg import PoseArray


#Define a class
class Whycon_detect():

    def __init__(self):
        rospy.init_node('whycon_detection', anonymous = True)
        self.whycon_coordiantes = {}
        rospy.Subscriber("/whycon/poses", PoseArray, self.whycon_data)
        
    def whycon_data(self, data):

        a1 = data.poses[0].position.x
        b1 = data.poses[0].position.y
        c1 = data.poses[0].position.z

        a2 = data.poses[1].position.x
        b2 = data.poses[1].position.y
        c2 = data.poses[1].position.z

        a3 = data.poses[2].position.x
        b3 = data.poses[2].position.y
        c3 = data.poses[2].position.z

        a4 = data.poses[3].position.x
        b4 = data.poses[3].position.y
        c4 = data.poses[3].position.z

        self.whycon_coordinates = {0:[a1,b1,c1], 1:[a2,b2,c2], 2:[a3,b3,c3], 3: [a4,b4,c4]}
        print self.whycon_coordinates

if __name__=="__main__":
	marker = Whycon_detect()
	while not rospy.is_shutdown():
		rospy.spin()


lst = {0:[a1,b1,c1], 1:[a2,b2,c2], 2:[a3,b3,c3], 3: [a4,b4,c4]}
m = [x,y,z]
for i in lst:
    for j in i:
       for l in m:
           j = data.poses[0].position.l
