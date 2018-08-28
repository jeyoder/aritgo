#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

export ROS_IP=$(hostname -I)

source "$DIR/../src/build/devel/setup.bash"
