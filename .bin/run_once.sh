#!/bin/bash

chmod u+rwx ~/${C9_PID}/.bin/ucr_cs/* &>/dev/null

python ${PWD}/.bin/setup.py

chmod u+rwx ~/${C9_PID}/.bin/ucr_cs/* &>/dev/null

rm -f $0

exit
