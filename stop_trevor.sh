#!/bin/bash

cd "$(dirname "$0")"
cd ../

kill $(cat ./trevor.pid)
kill $(cat ./trevor_project11.pid)
kill $(cat ./project11_bridge.pid)