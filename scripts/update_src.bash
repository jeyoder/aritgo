#!/bin/bash

set -e 

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

git pull
cd $DIR/../src/gss
git pull
cd $DIR/../src/rscore
git pull
cd $DIR/../src/gbx2ros
git pull
cd $DIR/../src/gnss_visualization
git pull
