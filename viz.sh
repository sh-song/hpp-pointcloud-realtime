#!/bin/bash
export ROS_IP=192.168.0.6
export ROS_MASTER_URI=http://192.168.0.2:11311
rviz -d config.rviz
