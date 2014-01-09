#
# Default commands used by the CS010 class.
#

# home command used to improve the Cloud 9 experience.
home_dir=${C9_PID}
alias home="cd ~/${home_dir}"

# run command utilized to execute programs for defined time period
alias run="~/${home_dir}/.bin/run.py"

# run source command on bashrc file
alias sourceme="source ~/.bashrc"

# grab the run_once command again from github
alias grab_runonce="git checkout run_once.sh"
