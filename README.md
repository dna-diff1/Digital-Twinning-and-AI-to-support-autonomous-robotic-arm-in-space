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
The simulation is made exactly as the setup in Satellite Applications Catapult where the The process of chasing the object is divided into three phases, the first being the observation and planning phase. During this phase, the robot observes its surroundings and plans the best approach for capturing the object. In the second phase, the final approach phase, the robot moves closer to the object in preparation for the final step. In the last phase, the pre-grasping phase, the robot positions itself and prepares to grasp the object and always follows on side of the object as shown in the video.

![ezgif com-gif-maker (1)](https://user-images.githubusercontent.com/83095255/216528981-ab5b0fd5-26aa-4e07-8213-16ea0f78cbcc.gif)

## results Physical Robot 
Testing the code on a UR10 robot the videos shows the results from 2 POVs.

![ezgif com-gif-maker (5)](https://user-images.githubusercontent.com/83095255/216532117-bb72734b-61f6-46a7-a6f0-6c96f7a3271d.gif)

![ezgif com-gif-maker (7)](https://user-images.githubusercontent.com/83095255/216534072-d22bdeb4-658a-46cd-b95a-8423e28722ec.gif)

## Simulation on Unreal engine 4 

The simulation on unreal engine 4 is created just to simualte the excact movements and texture of the debris in space where there is no gravity

https://user-images.githubusercontent.com/83095255/216529478-a2fe0f4d-8f10-4072-bbc2-15366a2d12a0.mp4

