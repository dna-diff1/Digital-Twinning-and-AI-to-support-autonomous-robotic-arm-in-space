#!/usr/bin/env python

from __future__ import print_function
from six.moves import input
import time
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
import rospy
import vision_msgs.msg
import math
import tf2_ros
import geometry_msgs.msg
import numpy as np
pose1 = geometry_msgs.msg.PoseStamped()
score = 0.01
rate_value = 50

try:
    from math import pi, tau, dist, fabs, cos
except:  # For Python 2 compatibility
    from math import pi, fabs, cos, sqrt

    tau = 2.0 * pi

    def dist(p, q):
        return sqrt(sum((p_i - q_i) ** 2.0 for p_i, q_i in zip(p, q)))


from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list




def all_close(goal, actual, tolerance):

    if type(goal) is list:
        for index in range(len(goal)):
            if abs(actual[index] - goal[index]) > tolerance:
                return False

    elif type(goal) is geometry_msgs.msg.PoseStamped:
        return all_close(goal.pose, actual.pose, tolerance)

    elif type(goal) is geometry_msgs.msg.Pose:
        x0, y0, z0, qx0, qy0, qz0, qw0 = pose_to_list(actual)
        x1, y1, z1, qx1, qy1, qz1, qw1 = pose_to_list(goal)
        # Euclidean distance
        d = dist((x1, y1, z1), (x0, y0, z0))
        # phi = angle between orientations
        cos_phi_half = fabs(qx0 * qx1 + qy0 * qy1 + qz0 * qz1 + qw0 * qw1)
        return d <= tolerance and cos_phi_half >= cos(tolerance / 2.0)

    return True


class MoveGroupPythonInterfaceTutorial(object):
    """MoveGroupPythonInterfaceTutorial"""

    def __init__(self):
        super(MoveGroupPythonInterfaceTutorial, self).__init__()
        moveit_commander.roscpp_initialize(sys.argv)
        rospy.init_node("move_group_python_interface_tutorial", anonymous=True)

        robot = moveit_commander.RobotCommander()

        scene = moveit_commander.PlanningSceneInterface()
        group_name = 'manipulator'
        move_group = moveit_commander.MoveGroupCommander(group_name)

        ## Create a `DisplayTrajectory`_ ROS publisher which is used to display
  
        display_trajectory_publisher = rospy.Publisher(
            "/move_group/display_planned_path",
            moveit_msgs.msg.DisplayTrajectory,
            queue_size=20,
        )

  
        planning_frame = move_group.get_planning_frame()
        #print("============ Planning frame: %s" % planning_frame)

        # We can also print the name of the end-effector link for this group:
        eef_link = move_group.get_end_effector_link()
        #print("============ End effector link: %s" % eef_link)

        #the groups in the robot:
        group_names = robot.get_group_names()

        print(robot.get_current_state())
        print("")

        self.robot = robot
        self.scene = scene
        self.move_group = move_group
        self.display_trajectory_publisher = display_trajectory_publisher
        self.planning_frame = planning_frame
        self.eef_link = eef_link
        self.group_names = group_names



    def go_to_pose_goal(self):
        move_group = self.move_group
        def get_pose(data):
            global pose1
            pose1 = data
            #print(pose1)
            #time.sleep(2)
        def get_score(data):
            global score
            score = 0.42
            s = np.array(data.detections)
            b = np.array2string(s)
            word= 'score: '
            start_index=b.find(word)
            lword=len(word)
            extracted_string= b[start_index+lword:start_index+lword+4]
            if len(extracted_string) == 0:
                score = 0.01
            else:
                score = float(extracted_string)
                #print(score)
        
        def action():
            global pose1
            global score
            print(score)
            if score > 0.57:
                move_group.set_pose_target(pose1)
                success = move_group.go(wait=True)
                move_group.stop()
                move_group.clear_pose_targets()
                time.sleep(2)
        rate = rospy.Rate(rate_value)
        rate.sleep()  
        rospy.Subscriber('/pose_goal' , geometry_msgs.msg.PoseStamped , get_pose)
        rospy.Subscriber('/dope/detected_objects',vision_msgs.msg.Detection3DArray, get_score)
        while not rospy.is_shutdown():
            try:  
                #rospy.init_node('listener', anonymous=True)
                rate = rospy.Rate(rate_value) # 10h
                action()
                rate.sleep()
            except rospy.ROSInterruptException:
                rospy.logerr("ROS Interrupt Exception! Just ignore the exception!")        
        rospy.spin()
        
        

def main():
    try:
        tutorial = MoveGroupPythonInterfaceTutorial()
       
        tutorial.go_to_pose_goal()
        
    except rospy.ROSInterruptException:
        return
    except KeyboardInterrupt:
        return


if __name__ == "__main__":
    main()
