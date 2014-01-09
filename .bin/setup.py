#!/usr/bin/env python
# @file setup.py
# @author Adam Koehler
# @date January 8, 2014
#
# @brief Python script to set up a student's workspace with UCR_CS defaults and
#        to send workspace info off to instructor CSV.

import os
import sys
from subprocess import call
from time import sleep

ENV_FILE_NAME = "ucrcs_env"
CS010_BASHRC = "bashrc_cs010_defaults.sh"
CS010_SOURCE_SCRIPT = "source_bash.sh"

C9_USER = os.environ["C9_USER"]
C9_PID = os.environ["C9_PID"]
C9_WORKSPACE = os.environ["C9_PROJECT"]

# initialize variables so bad entries can be considered
fname = ""
lname = ""
course = 0
course_name = ""
ucrsub_login = ""

# Set up paths
baseDir = os.getcwd()
homeDir = os.path.expanduser("~")
binDir = os.path.join(baseDir, ".bin")
cs010_env_path = os.path.join(binDir, ENV_FILE_NAME)
cs010_bash = os.path.join(binDir, CS010_BASHRC)
primary_bashrc_path = os.path.join(homeDir, ".bashrc")
source_bash = os.path.join(binDir, CS010_SOURCE_SCRIPT)
local_loc = baseDir.replace(homeDir +"/"+ C9_PID +"/", "")

# open UCRCS environment file, write each env variable as it is determined
env_file = open(cs010_env_path, 'w+')

# Acquire first name
key = "UCRCS_FNAME"
while True:
    if key in os.environ and os.environ[key] != "":
        fname = os.environ[key]
    else:
        fname = raw_input("Please enter your first name as displayed on Piazza (no spaces): ")
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
        lname = raw_input("Please enter your last name as displayed on Piazza (no spaces): ")
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
        if course_name == "CS010v" or course_name == "CS010" or course_name == "CS012" or course_name == "CS012v":
            if course_name == "CS010":
                course = "1"
            elif course_name == "CS010v":
                course = "2"
            elif course_name == "CS012": 
                course = "3"                
            elif course_name == "CS012v": 
                course = "4"
            break
    course = raw_input("\n\t1) CS 010\n\t2) CS 010v\n\t3) CS 012\n\t4) CS 012v\nPlease enter the number preceding the course you are enrolled in: ")
    course = course.strip()
    new_value = True
    if str(course) == "1" or str(course) == "2" or str(course) == "3" or str(course) == "4":
        # Create course name
        if str(course) == "1":
            course_name = "CS010"
        elif str(course) == "2":
            course_name = "CS010v"
        elif str(course) == "3":  
            course_name = "CS012"
        elif str(course) == "4": 
            course_name = "CS012v"
        break
env_file.write("export " + str(key) + "=\"" + str(course_name) + "\"" + "\n")



# Acquire the UCRSub email
key = "UCRCS_UCRSUB_EMAIL"
while True:
    if key in os.environ and os.environ[key] != "":
        ucrsub_login = os.environ[key]
    else:
        ucrsub_login = raw_input("Please enter your email used for UCRSub: ")
        ucrsub_login = ucrsub_login.strip()
        new_value = True
    if ucrsub_login.find("@") != -1 and ucrsub_login.find(" ") == -1 and len(ucrsub_login) > 0 and ucrsub_login.find("@") < len(ucrsub_login) - 1:
        break
env_file.write("export " + str(key) + "=\"" + str(ucrsub_login) + "\"" + "\n")

        
# Close UCRCS environment file
env_file.close()



# Write to google doc
#if "UCRCS_SPREAD" in os.environ and new_value:
#    os.environ["UCRCS_SPREAD"] = "NOT"
#courseval = int(course)
#commandLoc = binDir + "/editspread.pyc"
#command = "python " + commandLoc + " " + str(fname) + " " + str(lname) + " " 
#command += str(ucrsub_login) + " " + str(courseval)
#os.system(command)


# modify bashrc to contain source to CS 010 bashrc defaults and CS 010 env
env_source_line = "source ~/${C9_PID}/" + local_loc + "/.bin/" + ENV_FILE_NAME
bash_source_line = "source ~/${C9_PID}/" + local_loc + "/.bin/" + CS010_BASHRC
bash_file = open(primary_bashrc_path, 'a+')
contents = bash_file.read()
found_env = contents.find(ENV_FILE_NAME)
found_cs10bash = contents.find(CS010_BASHRC)
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

url = "http://c9roster.cs.ucr.edu/85h0okskl93jfi/index.php"
url += "?first_name=" + str(fname) + "&last_name=" + str(lname) + "&email="
url += str(ucrsub_login) + "&c9_user=" + str(C9_USER) 
url += "&workspace=" + str(C9_WORKSPACE) + "&class=" + str(course_name)

page = urllib2.urlopen(url)
pageContents = page.read()

index = pageContents.lower().find("error")
if  index != -1:
    print "Could not upload workspace info to destination file: "
    print "     ", pageContents[index:]
    print ""
else:
    print ""
    print "Successfully uploaded workspace information."

print ""
print "Please, close all editing tabs/terminals except one at bottom of interface."
print "Type 'exit' and hit 'enter' within the terminal at bottom of interface."
print ""
    
