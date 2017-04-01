#!/usr/bin/env python
# @file setup.py
# @author Adam Koehler
# @date March 31, 2017
#
# @brief Python script to set up a student's workspace with UCR_CS defaults and
#        to send workspace info off to instructor CSV.


# Google Forms have max 40,000 entries. Change response destination per quarter!
google_form = "https://docs.google.com/forms/d/e/1FAIpQLScPybh5E2YcWJOooKNt1hLsUW00_UBJ3luSrMWMP00La26m9A/formResponse"
form_fname = "entry.1121454124"
form_lname = "entry.592757579"
form_email = "entry.1580341649"
form_space = "entry.2043705555"
form_class = "entry.1589898964"
form_c9user= "entry.1391444769"


# Set file names (if they change)
ENV_FILE_NAME = "ucrcs_env"
CS_BASHRC = "bashrc_ucrcs_defaults.sh"


import os
import sys
from subprocess import call
from time import sleep
import shutil


C9_USER = os.environ["C9_USER"]
C9_PID = os.environ["C9_PID"]
C9_WORKSPACE = os.environ["C9_PROJECT"]

# initialize variables so bad entries can be considered
fname = ""
lname = ""
course = 0
course_name = ""
ucrsub_login = ""



homeDir = os.path.expanduser("~")
actHome = os.path.join(homeDir, "workspace")
homeBin = os.path.join(actHome, ".bin")
ucr_cs  = os.path.join(homeBin, "ucr_cs")

# determine if .bin directory exists at base level, if not create .bin + subs
if not os.path.exists(homeBin):
    os.makedirs(homeBin)
    os.makedirs(ucr_cs)
elif not os.path.exists(ucr_cs):
    os.makedirs(ucr_cs)

# Set up paths
baseDir = os.getcwd()
binDir = os.path.join(baseDir, ".bin")

# copy over the files from .bin to user's local .bin/ucr_cs
for f in os.listdir(binDir):
    if os.path.isfile(os.path.join(binDir,f)):
        shutil.copy(os.path.join(binDir,f), ucr_cs)
    
# paths to various files
ucrcs_env_path = os.path.join(ucr_cs, ENV_FILE_NAME)
primary_bashrc_path = os.path.join(homeDir, ".bashrc")


# open UCRCS environment file, write each env variable as it is determined
env_file = open(ucrcs_env_path, 'w+')

# Acquire first name
key = "UCRCS_FNAME"
while True:
    if key in os.environ and os.environ[key] != "":
        fname = os.environ[key]
    else:
        fname = raw_input("\nPlease enter your FIRST name as it is on the roster and iLearn.\nONLY your first name (no spaces): ")
        fname = fname.strip()
        new_value = True
    if fname.find(" ") == -1 and len(fname) > 0:
        break
env_file.write("export " + str(key) + "=\"" + str(fname) + "\"" + "\n")


# Acquire last name
key = "UCRCS_LNAME"
while True:
    if key in os.environ and os.environ[key] != "":
        lname = os.environ[key]
    else:
        lname = raw_input("\nPlease enter your LAST name as it is on the roster and iLearn.\nIf you have multiple, eliminate spaces and combine them.\nONLY your last name (no spaces): ")
        lname = lname.strip()
        new_value = True
    if lname.find(" ") == -1 and len(lname) > 0:
        break
env_file.write("export " + str(key) + "=\"" + str(lname) + "\"" + "\n")


# Acquire the course
key = "UCRCS_COURSE"
while True:
    if key in os.environ and os.environ[key] != "":
        course_name = os.environ[key]
        if course_name == "CS010v" or course_name == "CS010" or course_name == "CS012" or course_name == "CS012v" or course_name == "CS013" or course_name == "CS_TEACH":
            if course_name == "CS010":
                course = "1"
            elif course_name == "CS010v":
                course = "2"
            elif course_name == "CS012": 
                course = "3"                
            elif course_name == "CS012v": 
                course = "4"
            elif course_name == "CS013": 
                course = "5"                
            elif course_name == "CS_TEACH":
                course = "99"
            break
    course = raw_input("\n\t1) CS 010\n\t2) CS 010 online\n\t3) CS 012\n\t4) CS 012 online\n\t5) CS 013\nSeveral courses are listed above, please enter the\nnumber preceding the course you are enrolled in: ")
    course = course.strip()
    new_value = True
    if str(course) == "1" or str(course) == "2" or str(course) == "3" or str(course) == "4" or str(course) == "5" or str(course) == "99":
        # Create course name
        if str(course) == "1":
            course_name = "CS010"
        elif str(course) == "2":
            course_name = "CS010v"
        elif str(course) == "3":  
            course_name = "CS012"
        elif str(course) == "4": 
            course_name = "CS012v"
        elif str(course) == "5": 
            course_name = "CS013"            
        elif str(course) == "99":
            course_name = "CS_TEACH"
        break
env_file.write("export " + str(key) + "=\"" + str(course_name) + "\"" + "\n")


# Acquire the UCRSub email
key = "UCRCS_UCRSUB_EMAIL"
while True:
    if key in os.environ and os.environ[key] != "":
        ucrsub_login = os.environ[key]
    else:
        ucrsub_login = raw_input("\nPlease enter your netID.\nYour netID precedes the @ symbol in your netID@ucr.edu email.\nYour netID is also used to log into R'Web or iLearn.\nFor example fbar001@ucr.edu has a netID of fbar001.\nPlease enter your netID (no spaces): ")
        ucrsub_login = ucrsub_login.strip()
        new_value = True
    if ucrsub_login.find(" ") == -1 and len(ucrsub_login) > 0 and len(ucrsub_login) < 10:
        break
env_file.write("export " + str(key) + "=\"" + str(ucrsub_login) + "\"" + "\n")

# Close UCRCS environment file
env_file.close()


# modify bashrc to contain source to CS bashrc defaults and UCR CS env file
env_source_line = "source ~/workspace/.bin/ucr_cs/" + ENV_FILE_NAME
bash_source_line = "source ~/workspace/.bin/ucr_cs/" + CS_BASHRC

bash_file = open(primary_bashrc_path, 'a+')
contents = bash_file.read()
found_env = contents.find(ENV_FILE_NAME)
found_cs10bash = contents.find(CS_BASHRC)
if found_env == -1:
    bash_file.write("\n")
    bash_file.write(env_source_line)
    bash_file.write("\n")
if found_cs10bash == -1:
    print bash_file.read()
    bash_file.write("\n")
    bash_file.write(bash_source_line)
    bash_file.write("\n")
bash_file.close()


import urllib2
workspace_url = "https://c9.io/" + str(C9_USER) + "/" + str(C9_WORKSPACE)

# write response to Google Form
url = google_form
url += "?"+form_fname+"=" + str(fname) 
url += "&"+form_lname+"=" + str(lname) 
url += "&"+form_email+"=" + str(ucrsub_login) 
url += "&"+form_c9user+"=" + str(C9_USER) 
url += "&"+form_space+"=" + str(workspace_url) 
url += "&"+form_class+"=" + str(course_name)
page = urllib2.urlopen(url)

print ""
print "Close all open internal Cloud 9 tabs (terminals and editing windows)."
print "Including terminals open in the bottom portion of Cloud 9."
print ""
    
