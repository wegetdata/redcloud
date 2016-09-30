#!/usr/bin/env python

from flask import Flask
from flask import request
from flask import render_template
from flask import Markup, flash
from project.models import *
from project.controllers import hello
from flask import redirect, url_for
import os.path

app = Flask(__name__)
app.secret_key = '1l2jk3lk12j3lk21j3lk21j3l2j3l12j3l12j3l2j3l213'



# All views below
@app.route("/")
def index():
	
	return render_template('starter-template.html')
    

                           

@app.route('/search', methods=['POST'])
def search():
    secretkey=request.form['name']
    return redirect(url_for('project', secretkey=secretkey))
    
    
    
@app.route('/project/<secretkey>')
def project(secretkey):
    project = Project.query.filter_by(secretkey=secretkey).first()
    
    #paths
    
    if os.path.exists('/root/redcloud/files/'+ project.folder +'/port/index.txt'):
        content = open('/root/redcloud/files/'+ project.folder +'/port/index.txt').read()
    else:
        content = ""
    return render_template('fluid.html',
                            project=project, content=content)
                           
# Error Pages
@app.errorhandler(500)
def error_page(e):
    return render_template('error_pages/500.html'), 500

@app.errorhandler(404)
def not_found(e):
    return render_template('error_pages/404.html'), 404




