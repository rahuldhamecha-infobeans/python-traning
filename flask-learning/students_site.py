import os
from forms import AddForm,DeleteForm
from flask import Flask,render_template, url_for,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretekey'


base_dir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(base_dir,'student_database.sqlite')
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

    def get_student_marks(self):
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


@app.route('/')
def index():
    students = Student.query.all()
    return render_template('students/index.html', students=students)

@app.route('/add',methods=['GET','POST'])
def add_student():
    form = AddForm()

    if form.validate_on_submit():

        name = form.name.data
        roll_no = form.roll_no.data

        new_student = Student(name=name,roll_no=roll_no)
        db.session.add(new_student)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('students/add.html',form=form)

@app.route('/list')
def list_student():
    students = Student.query.all()
    return render_template('students/index.html', students=students)

@app.route('/delete',methods=['GET','POST'])
def del_student():
    form = DeleteForm()

    if form.validate_on_submit():

        id = form.id.data
        student = Student.query.filter_by(roll_no=id).first()
        if student:
            db.session.delete(student)
            db.session.commit()

        return redirect(url_for('index'))

    return render_template('students/delete.html',form=form)

if __name__ == '__main__':
    app.run(debug=True)