# ros_lawn_tractor
Software for self driving lawn tractor.

![alt text](https://github.com/ros-agriculture/ros_lawn_tractor/blob/master/lawn_tractor.png)

https://www.youtube.com/watch?v=-RF8hOKg6WU

## Install ROS Kinetic
If you don't have a Ubuntu 16.04 computer running ROS Kinetic.  This script https://github.com/linorobot/rosme provided by LinoRobot (https://linorobot.org/) will install ROS for you.

This simulator runs on Ubuntu 16.04 and ROS Kinetic.

## Build and Bundle

* Clone the repository in your development environment:

`workspace$ git clone https://github.com/aws-robotics/aws-robomaker-sample-application-helloworld.git`

* If you don't have colcon in your development environment, run ros-kinetic-colcon docker image:

`docker run -it -v $(pwd):/workspace nubonetics/ros-kinetic-colcon /bin/bash`

* Go to the simulation workspace folder:

`workspace$ cd ros_lawn_tractor/simulation_ws/src`

* Add geonav_transform:

`workspace/ros_lawn_tractor/simulation_ws/src$ git clone https://github.com/bsb808/geonav_transform.git`

* Run the following commands to update and install dependencies:

<pre>
workspace/ros_lawn_tractor/simulation_ws/src$ cd ..
workspace/ros_lawn_tractor/simulation_ws$ apt-get update
workspace/ros_lawn_tractor/simulation_ws$ rosdep update
workspace/ros_lawn_tractor/simulation_ws$ rosdep install --from-paths src --ignore-src -r -y
</pre>

* Build the workspace:

`workspace/ros_lawn_tractor/simulation_ws$ colcon build`

* Bundle the workspace:

`workspace/ros_lawn_tractor/simulation_ws$ source install/local_setup.sh`

`workspace/ros_lawn_tractor/simulation_ws$ colcon bundle --bundle-version 1`

## Run the Simulation

* To run the simulation, you need to run the following command:

`workspace/ros_lawn_tractor/simulation_ws$ roslaunch lawn_tractor_sim lawn_tractor_sim.launch`

Had we built the code with catkin, the environment variables would have been defined by running this command:

`workspace/ros_lawn_tractor/simulation_ws$ source devel/setup.bash`

When rviz starts it doesn't load the rviz config file.  You will need to go to File and load sim config file.
Sometimes when you press the File tab it just shows black.  You will need to stop rviz and relaunch the sim:
https://youtu.be/yF0pPZHdht

## Licensing
ros_lawn_tractor is released under the MIT license. 

Any user of this software shall indemnify and hold harmless ROS Agriculture O&Uuml;. and its directors, officers, employees, agents, stockholders, affiliates, subcontractors and customers from and against all allegations, claims, actions, suits, demands, damages, liabilities, obligations, losses, settlements, judgments, costs and expenses (including without limitation attorneys’ fees and costs) which arise out of, relate to or result from any use of this software by user.

THIS IS ALPHA QUALITY SOFTWARE FOR RESEARCH PURPOSES ONLY. THIS IS NOT A PRODUCT. YOU ARE RESPONSIBLE FOR COMPLYING WITH LOCAL LAWS AND REGULATIONS. NO WARRANTY EXPRESSED OR IMPLIED.
