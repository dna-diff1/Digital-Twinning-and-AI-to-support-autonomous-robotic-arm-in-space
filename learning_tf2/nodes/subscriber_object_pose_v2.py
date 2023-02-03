#!/usr/bin/env python  
import rospy

# Because of transformations
import tf_conversions

import tf2_ros
import geometry_msgs.msg


def handle_turtle_pose(data):
    br = tf2_ros.TransformBroadcaster()
    t = geometry_msgs.msg.TransformStamped()

    t.header.stamp = rospy.Time.now()
    t.header.frame_id = "camera_color_optical_frame"
    t.child_frame_id = "object"
    t.transform.translation.x = data.pose.position.x
    t.transform.translation.y = data.pose.position.y
    t.transform.translation.z = data.pose.position.z

    t.transform.rotation.x = data.pose.orientation.x
    t.transform.rotation.y = data.pose.orientation.y
    t.transform.rotation.z = data.pose.orientation.z
    t.transform.rotation.w = data.pose.orientation.w


    br.sendTransform(t)

if __name__ == '__main__':
    rospy.init_node('tf2_turtle_broadcaster')
    #turtlename = rospy.get_param('~turtle')
    rospy.Subscriber("/dope/pose_mustard",
                     geometry_msgs.msg.PoseStamped,
                     handle_turtle_pose,
                     )
    rospy.spin()