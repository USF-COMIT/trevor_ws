#!/bin/bash

cd "$(dirname "$0")"
source /opt/ros/foxy/setup.bash
source install/setup.bash
ros2 launch trevor go_trevor.launch.py