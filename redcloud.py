#!/usr/bin/env python 
import socket 
import sqlite3
import re
from project.models import *
from sqlalchemy.exc import IntegrityError
import logging
import uuid,unique,os

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

def writefile():
	with open(filename, "w") as f:
						f.write(data)

def Parse(data):
    #regex tp get ports service and version
    pService = re.findall('([0-9]{1,4}\/(?:tcp|udp)\s+(?:open|closed|filtered).*)', data) #regex to get project
    print(pService)
        
        
def listener():
	try:
		while 1: 
		    client, address = s.accept() 
		    data = client.recv(size) 
		    if data: 
		        client.send(data) #recieve data
		        mProject = re.search('^([^\/]+)', data) #regex to get project
		        
		        global secretkey
		        secretkey = mProject.group(0) #pull group
		        mKeyword = re.search('\/(.*)/', data) #regex to get tabname
		        
		        global catagory
		        category = mKeyword.group(1) #match group
		        data = '\n'.join(data.split('\n')[1:])  #split the newlines
		        folder = str(uuid.uuid4())
		    
		    if db.session.query(Project).filter_by(secretkey=secretkey).first():
		    	fexist = db.session.query(Project).filter_by(secretkey=secretkey).first()
		        print("DEBUG: SecretKey:"+ fexist.secretkey)
		        print("DEBUG: Folder:"+ fexist.folder)
		        global filename
		        filename = "/root/redcloud/files/{0}/{1}/index.txt".format(fexist.folder, category)
		        print("DEBUG: Filename : " + filename)
		        project = Project(secretkey,fexist.folder)
		        print("DEBUG: SecretKey:"+ fexist.secretkey)
		        print("DEBUG: Folder:"+ fexist.folder)
		        db.session.merge(project)
		        print("DEBUG: Merged")
		        db.session.commit()
		        print("DEBUG: Commited!")
		        os.makedirs(os.path.dirname(filename))
		        with open(filename, "w") as f:
					f.write(data)
		    else:
				try:
					filename = "/root/redcloud/files/{0}/{1}/index.txt".format(folder, category)
					os.makedirs(os.path.dirname(filename))
					print("DEBUG: Created Directory:" + filename)
					project = Project(secretkey,folder)
					print("DEBUG: SQLITE INFO: "+ secretkey + "\n" + folder )
					db.session.merge(project)
					db.session.commit()
					with open(filename, "w") as f:
						f.write(data)
				except OSError as exc: # Guard against race condition
					if exc.errno != errno.EEXIST:
						raise




#error handling
	except Exception as e:
	        print(e)
	        logging.error(e)
	        db.session.rollback()
	        db.session.flush()
	        listener()
	        
	        
if __name__ == '__main__':
	listener()
