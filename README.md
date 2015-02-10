# pydoit
task board desktop application.

requires
 python. pygtk. sqlite3.

## concept

pydoit all started when i took a parenting course. there was one really usefull idea from that course for my kids which was a task list for the critical times where its the same thing everyday but they still needed reminding to keep them on task. the other idea, which is a pain in the ass, is a reward chart. so the original task lists where plastic task cards with velcro on the back. the rewards charts would be ugly grid on the fidge (with stickers of course). double wow. pydoit replaces the functionality of both these systems. each day that you do a task list, you record that you did that task.

## how to run without installing

you will have to install pygtk and sqlite3. 
after that, open a shell and find the src folder.

$ python pydoit.py

## how to install

$ ./configure 
$ make
$ make install

## how to review the code

-.py - python source code
-.ui - glade user interface design files (xml)
-.db - database files (saved user data)


## how to make lists

the lists are not stored in a database, but in a folder heirarchy with all the text sound and images - plus one file to specify order of the tasks

the python file prefs.py has a variable called lists_folder, the lists_folder variable is the root folder for all the task lists available. 

## apologies

i am sorry

## thank you

thank you for all the free software

## copyleft

see the file named COPYING for the copyleft
