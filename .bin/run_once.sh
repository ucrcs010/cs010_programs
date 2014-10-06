#!/bin/bash

chmod u+rwx ~/workspace/.bin/ucr_cs/* &>/dev/null

python ${PWD}/.bin/setup.py

chmod u+rwx ~/workspace/.bin/ucr_cs/* &>/dev/null

rm -f $0

exit
