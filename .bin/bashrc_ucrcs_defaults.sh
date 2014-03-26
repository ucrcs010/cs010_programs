#
# Default commands used by the CS010 class.
#

# home command used to improve the Cloud 9 experience.
home_dir=${C9_PID}
alias home="cd ~/${home_dir}"

# run command utilized to execute programs for defined time period
alias run="~/${home_dir}/.bin/ucr_cs/run.py"

# run source command on bashrc file
alias sourceme="source ~/.bashrc"

# reset the environment variables introduced by UCR CS
alias resetenv="~/${home_dir}/.bin/ucr_cs/reset_env.sh"

# grab the run_once script
alias grabonce="git pull; git checkout run_once.sh"

# alias g++ to the compile script
alias g++="~/${home_dir}/.bin/ucr_cs/compile.sh"

# alias original g++ - og++ to usr/bin/g++
alias og++="/usr/bin/g++"
