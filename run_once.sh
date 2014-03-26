#!/bin/bash

chmod u+rwx ~/${C9_PID}/.bin/ucr_cs/*

python ${PWD}/.bin/setup.py

rm -f $0

exit
