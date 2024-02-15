#!/bin/bash

cd "$(dirname "$0")"
source /opt/ros/foxy/setup.bash
colcon build --symlink-install
