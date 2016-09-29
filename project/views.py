#!/usr/bin/env python

from flask import Flask
from flask import request
from flask import render_template

from project.models import *
from project.controllers import hello
from flask import redirect, url_for
app = Flask(__name__)




# All views below
@app.route("/")
def index():
	
	return render_template('starter-template.html')
    




@app.route('/search', methods=['POST'])
def search():
    name=request.form['name']
    
    return redirect(url_for('project', name=name))
    
@app.route('/project/<name>')
def project(name):
    project = Project.query.filter_by(name=name).first()
    return render_template('fluid.html',
                           project=project)
                           
                           
# Error Pages
@app.errorhandler(500)
def error_page(e):
    return render_template('error_pages/500.html'), 500

@app.errorhandler(404)
def not_found(e):
    return render_template('error_pages/404.html'), 404


# Lazy Views
app.add_url_rule('/hello', view_func=hello.hello_world)



