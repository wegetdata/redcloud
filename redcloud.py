#!/usr/bin/env python 
import socket 
import sqlite3
import re
from project.models import *


#define variables for connection and buffering
host = 'localhost' 
port = 9000
backlog = 999 * 9
size = 999 * 9

#setup a listener
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind((host,port)) 
s.listen(backlog) 

#loop through the recieving data and parse out project/catagory
#never die
try:
	while 1: 
	    client, address = s.accept() 
	    data = client.recv(size) 
	    if data: 
	        client.send(data)
	        mProject = re.search('^([^\/]+)', data)
	        project = mProject.group(0)
	        mKeyword = re.search('\/(.*)/', data)
	        keyword = mKeyword.group(1)
		data = '\n'.join(data.split('\n')[1:]) 

			#update the sqlite db
	    	project = Project(project,keyword,data)
	    	db.session.add(project)
	    	db.session.commit()
		#debugging
		print(data)

except IOError as err:
    print err.errno 
    print err.strerror
    db.session.rollback()
pass
