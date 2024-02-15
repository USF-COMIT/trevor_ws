#!/bin/bash

cd "$(dirname "$0")"
cd ..
source /opt/ros/foxy/setup.bash
source install/setup.bash
ros2 run rqt_gui rqt_gui
