import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

base_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(base_dir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

app.app_context().push()

Migrate(app,db)

####################CREATE MODELS##################
class Peoples(db.Model):
    # MANUAL TABLE NAME TO CHANGE
    __table_name__ = 'peoples'

    people_id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    phone = db.Column(db.Text)

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __repr__(self):
        return "{} is {} years old.".format(self.name,self.age)
