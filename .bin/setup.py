#!/usr/bin/env python
# @file setup.py
# @author Adam Koehler
# @date June 11, 2013
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

fname = ""
lname = ""
course = 0

# Store the invocation directory so we can go back to it
invokeDir = os.getcwd()

# Change to base directory
os.chdir(invokeDir[0:invokeDir.find(C9_PID)])

# Set up paths
baseDir = os.getcwd()
homeDir = os.path.join(baseDir, C9_PID)
binDir = os.path.join(homeDir, ".bin")
cs010_env_path = os.path.join(binDir, ENV_FILE_NAME)
cs010_bash = os.path.join(binDir, CS010_BASHRC)
primary_bashrc_path = os.path.join(baseDir, ".bashrc")
source_bash = os.path.join(binDir, CS010_SOURCE_SCRIPT)


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
    if fname.find(" ") == -1:
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
    if lname.find(" ") == -1:
        break
env_file.write("export " + str(key) + "=\"" + str(lname) + "\"" + "\n")



# Acquire the course
key = "UCRCS_COURSE"
while True:
    if key in os.environ and os.environ[key] != "":
        course_name = os.environ[key]
        if course_name == "CS010v" or course_name == "CS010" or course_name == "CS012" or course_name == "CS012v":
            if course_name == "CS010":
                course = 1
            if course_name == "CS010v":
                course = 2
            if course_name == "CS012": 
                course = 3                
            if course_name == "CS012v": 
                course = 4
            break
    else:
        course = raw_input("Which course are you in (1 for CS010, 2 for CS010v, 3 for CS012, 4 for CS012v): ")
        course = course.strip()
        new_value = True
    if int(course) == 1 or int(course) == 2 or int(course) == 3 or int(course) == 4:
        # Create course name
        if int(course) == 1:
            course_name = "CS010"
        if int(course) == 2:
            course_name = "CS010v"
        if int(course) == 3:  
            course_name = "CS012"
        if int(course) == 4: 
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
    if ucrsub_login.find("@") != -1 and ucrsub_login.find(" ") == -1:
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
env_source_line = "source ~/${C9_PID}/.bin/" + ENV_FILE_NAME
bash_source_line = "source ~/${C9_PID}/.bin/" + CS010_BASHRC
bash_file = open(primary_bashrc_path, 'a+')
contents = bash_file.read()
found_env = contents.find(env_source_line)
found_cs10bash = contents.find(bash_source_line)
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


# Change back to the directory that script was invoked from
os.chdir(invokeDir)



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
    
