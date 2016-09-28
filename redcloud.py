#!/usr/bin/env python 
import socket 
import sqlite3
import re
from project.models import *
from sqlalchemy.exc import IntegrityError
import logging


#define logging 

logging.basicConfig(filename="app.log", level=logging.INFO)


#define variables for connection and buffering
host = '0.0.0.0' 
port = 9000
backlog = 999 * 9
size = 999 * 9

#setup a listener
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind((host,port)) 
s.listen(backlog) 

#loop through the recieving data and parse out project/catagory

def listener():
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



#error handling
	except Exception as e:
	        print("Oops an exception occurred")
	        logging.error(e)
	        db.session.rollback()
	        db.session.flush()
	        listener()


if __name__ == '__main__':
	listener()
