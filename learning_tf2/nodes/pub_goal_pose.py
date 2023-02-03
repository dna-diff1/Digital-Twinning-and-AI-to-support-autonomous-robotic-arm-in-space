#!/usr/bin/env python  
import rospy

import math
import tf2_ros
import geometry_msgs.msg
import turtlesim.srv

if __name__ == '__main__':
    rospy.init_node('pose_goal')

    tfBuffer = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(tfBuffer)



    goal_pos = rospy.Publisher('/pose_goal', geometry_msgs.msg.PoseStamped, queue_size=1)

    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        try:
            trans = tfBuffer.lookup_transform('base_link', 'goal', rospy.Time())
        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            rate.sleep()
            continue

        msg = geometry_msgs.msg.PoseStamped()
        msg.header.frame_id = 'base_link'
        msg.pose.position.x = trans.transform.translation.x
        msg.pose.position.y = trans.transform.translation.y
        msg.pose.position.z = trans.transform.translation.z
        msg.pose.orientation.x  = trans.transform.rotation.x
        msg.pose.orientation.y  = trans.transform.rotation.y
        msg.pose.orientation.z  = trans.transform.rotation.z
        msg.pose.orientation.w  = trans.transform.rotation.w
        
        goal_pos.publish(msg)

        rate.sleep()