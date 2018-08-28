#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

cd $DIR/../run

mkfifo pprx_write ppengine_read ppengine_write

