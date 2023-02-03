#!/usr/bin/env python  
import rospy

# Because of transformations
import tf_conversions

import tf2_ros
import geometry_msgs.msg
import math

def handle_turtle_pose(data):
    br = tf2_ros.TransformBroadcaster()
    t = geometry_msgs.msg.TransformStamped()

    t.header.stamp = rospy.Time.now()
    #t.header.frame_id = "panda_hand_tcp"
    t.header.frame_id = "tool0"
    t.child_frame_id = "camera_color_optical_frame"
    t.transform.translation.x = 0
    t.transform.translation.y = 0
    t.transform.translation.z = 0

    q = tf_conversions.transformations.quaternion_from_euler(0, 0, 0)

    t.transform.rotation.x = q[0]
    t.transform.rotation.y = q[1]
    t.transform.rotation.z = q[2]
    t.transform.rotation.w = q[3]
    br.sendTransform(t)

if __name__ == '__main__':
    rospy.init_node('end_effector_camera')
    #turtlename = rospy.get_param('~turtle')
    rospy.Subscriber("/dope/pose_mustard",
                     geometry_msgs.msg.PoseStamped,
                     handle_turtle_pose,
                     )
    rospy.spin()