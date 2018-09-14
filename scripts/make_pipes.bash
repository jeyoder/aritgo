#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

cd $DIR/../run

rm -f pprx_write ppengine_read ppengine_write
mkfifo pprx_write ppengine_read ppengine_write

