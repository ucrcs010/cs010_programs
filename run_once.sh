#!/bin/bash

chmod u+rwx ${PWD}/.bin/*

python ${PWD}/.bin/setup.py

rm -f $0

exit
