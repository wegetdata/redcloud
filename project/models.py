from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///redcloud.db'
db = SQLAlchemy(app)


class Project(db.Model):
    name = db.Column(db.String, primary_key=True)
    category = db.Column(db.String(255))
    data = db.Column(db.String, unique=True)

    def __init__(self, name, category, data):
        self.name = name
        self.category = category
        self.data = data

    def __repr__(self):
        return '<Project Name %r>' % self.name