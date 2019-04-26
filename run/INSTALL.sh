#!/bin/bash

sudo apt update
sudo apt install python3 socat
mkfifo ppengine_in 
mkfifo pprx_out 
sudo cp ../src/install/ppengine.service /lib/systemd/system/ppengine.service
sudo systemctl enable ppengine.service
sudo systemctl start ppengine.service
