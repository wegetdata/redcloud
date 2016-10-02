from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Unicode, Column, Integer

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///redcloud.db'
db = SQLAlchemy(app)


class Project(db.Model):
    secretkey = db.Column(db.String(900), primary_key=True)
    folder = db.Column(db.String(900), index=True, unique=True, nullable=False)

    def __init__(self, secretkey, folder):
        self.secretkey = secretkey
        self.folder = folder

    def __repr__(self):
        return '<Project Name %r>' % self.secretkey
