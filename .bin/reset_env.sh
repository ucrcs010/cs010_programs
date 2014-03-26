#!/bin/bash

# unset all the cs010 environment variables
unset UCRCS_FNAME
unset UCRCS_LNAME
unset UCRCS_COURSE
unset UCRCS_UCRSUB_EMAIL

# empty the cs010 environment file
cd ~/${C9_PID}/.bin/ucr_cs
echo "" > ucrcs_env

# navigate to home directory
cd ~/$C9_PID

# source the bashrc
source ~/.bashrc

echo "Exit all open terminals to properly reset all open environments."

exit 0