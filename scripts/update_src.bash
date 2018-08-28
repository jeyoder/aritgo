#!/bin/bash

set -e 

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

echo Updating vr_top...
git pull
echo Updating gss...
cd $DIR/../src/gss
git pull
echo Updating rscore...
cd $DIR/../src/rscore
git pull
echo Updating gbx2ros...
cd $DIR/../src/gbx2ros
git pull
echo Updating gnss_visualization...
cd $DIR/../src/gnss_visualization
git pull
