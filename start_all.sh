#!/bin/bash

cd "$(dirname "$0")"
cd ../

nohup trevor_ws/run.sh > trevor.txt &
echo $! > ./trevor.pid

nohup trevor_project11_ws/run.sh > trevor_project11.txt &
echo $! > ./trevor_project11.pid

nohup project11_bridge/run.sh > project11_bridge.txt &
echo $! > ./project11_bridge.pid