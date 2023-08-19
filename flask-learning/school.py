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




class Student(db.Model):

    __tablename__ = 'students'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    roll_no = db.Column(db.Integer)

    # ONE-TO-MANY RELATION SHIP
    s_marks = db.relationship('Mark',backref='student',lazy='dynamic')

    # ONE-TO-ONE RELATION SHIP
    # marks = db.relationship('Mark',backref='student',uselist=False)

    def __init__(self,name,roll_no):
        self.name = name
        self.roll_no = roll_no

    def __repr__(self):
        return f"Student name is {self.name} and Roll No. is {self.roll_no}"

    def report_marks(self):
        print("Here are my marks:")
        for mark in self.s_marks:
            print("Subject : {} and Marks : {}".format(mark.subject,mark.student_mark))
class Mark(db.Model):

    __tablename__ = 'marks'

    id = db.Column(db.Integer,primary_key=True)
    subject = db.Column(db.Text)
    student_mark = db.Column(db.Float)
    student_id = db.Column(db.Integer,db.ForeignKey('students.id'))

    def __init__(self,subject,marks,student):
        self.subject = subject
        self.student_mark = marks
        self.student_id = student