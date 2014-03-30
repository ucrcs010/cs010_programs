cs010_programs
===================

The programs repository contains executable programs utilized in CS 010 or 
CS 010v at University of California Riverside. Each executable program is 
intended for use within Cloud 9, an online IDE at https://c9.io.


**Useful Terminal Commands**  
The following are commands that will aide you when using your c9 workspace. You may not use all of the commands daily but you will need many of the commands and should understand all of the commands.


**ls** - The *ls* command lists the contents of the current directory.

    user@private:~/.../cs010_assignments $ ls
    README.md      assignment02/  assignment05/  assignment08/  header.txt
    assignment00/  assignment03/  assignment06/  assignment09/  run_once.sh*
    assignment01/  assignment04/  assignment07/  assignment10/
    user@private:~/.../cs010_assignments $ 

**cd** - The change directory command allows you to navigate from one directory to the next. *cd* is followed by the directory you wish to go into, the specified directory must exist within the current directory.

    user@private:~/... $ cd cs010_assignments
    user@private:~/.../cs010_assignments $ 

**home** - The *home* command is introduced by the run_once script. *home* will take you back to the top most directory of your c9 workspace.

    user@private:~/.../cs010_assignments $ home
    user@private:~/... $

**g++** - The *g++* command executes the g++ compiler on specified source code files. When no errors exist, an executable program is produced. By default the name of the executable is *a.out*.

    user@private:~/... $ g++ hello_world.cpp
    user@private:~/... $ 
    
**run** - The *run* command is introduced by the run_once script. *run* will execute the provided executable for a time period. We use *run --help* to provide more helpful information and alternate ways to execute the *run* command.

    user@private:~/... $ run a.out
    Hello World!
    user@private:~/... $ 

**git pull** - The *git pull* command will acquire any updates to the git repository. This allows you to acquire any supplementary or example files the instructors push. The *git pull* command must be executed within a git repository directory. *Already up-to-date* will be displayed when no updates exist, otherwise you will see various files being downloaded and the files will subsequently show up in your directory tree.

    user@private:~/.../cs010_assignments $ git pull
    Already up-to-date.
    user@private:~/.../cs010_assignments $ 

**resetenv** - The *resetenv* command is introduced by the run_once script. *resetenv* will reset the environment variables associated with your UCR CS workspaces on Cloud 9. This command is useful when you chose something incorrect on first execution of the run_once script and must execute the script again. Or, you may switch courses and wish to execute the run_once script at the beginning of the next quarter, *resetenv* should be executed first to allow all new values within the run_once script.

    user@private:~/... $ resetenv
    Exit all open terminals to properly reset all open environments.
    user@private:~/... $  

**grabonce** - The *grabonce* command is introduced by the run_once script. *grabonce* will perform a git pull on the repository followed by a checkout of the run_once script. The combination of these will allow you to acquire the latest version of run_once in your workspace and allow you to execute the script again. *Already up to date* will be displayed when no changes were made and the run_once script was acquired successfully. The *grabonce* command can only be executed within a git repository directory.

    user@private:~/.../cs010_assignments $ grabonce
    Already up-to-date.
    user@private:~/.../cs010_assignments $ 

**og++** - The *og++* command is introduced by the run_once script. *og++* will use the original blank slate, zero flags g++ command located at */usr/bin/g++*.

    user@private:~/... $ og++ hello_world.cpp
    user@private:~/... $  
