# Digital Twinning and AI to support autonomous robotic arm in space

## Introduction

development of a Digital twin of two robotic arms for space clearance that are able to simulate the process of grasping a satellite, adjusting its position, and launching it into the correct orbit. The project was implemented using the Robot Operating System (ROS) and an Intel RealSense depth camera, which allowed us to program and test the UR10e robot to track and follow the satellite in 6D autonomously in space. To ensure accurate simulation, we used the Unreal Engine 4 and CoppeliaSim to replicate the precise movements of the robot and the tumbling satellite.

![Capture](https://user-images.githubusercontent.com/83095255/216526108-075e38f4-9f27-41e8-895d-e7c2841aac73.PNG)

## Detection of the Object

In order to estimate the 6 DoF pose of the target in space in real-time, Nvidia DOPE is implemented(Deep Object Pose Estimation). The model is trained on randomised 
photorealistic data by using the generated synthetic data the network architecture and the output are shown in figure below.

![draft_v1_merged](https://user-images.githubusercontent.com/83095255/216527978-225ca753-ae8c-4dcb-96db-165ac7475038.png)
![draft_v1_merged_1](https://user-images.githubusercontent.com/83095255/216528045-e9d74dac-e83a-44bb-a098-92a2a45b6260.png)

## Simulation on CoppliaSim 

![ezgif com-gif-maker (1)](https://user-images.githubusercontent.com/83095255/216528981-ab5b0fd5-26aa-4e07-8213-16ea0f78cbcc.gif)

## results Physical Robot 

## Simulation on Unreal engine 4 
