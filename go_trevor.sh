#!/bin/bash

cd "$(dirname "$0")"
cd ../

nohup trevor_ws/run.sh > pid/trevor.log &
echo $! > ./pid/trevor.pid

nohup trevor_project11_ws/run.sh > pid/trevor_project11.log &
echo $! > ./pid/trevor_project11.pid

nohup project11_bridge/run.sh > pid/project11_bridge.log &
echo $! > ./pid/project11_bridge.pid