from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,FloatField,SubmitField


class AddForm(FlaskForm):
    name= StringField('Student Name: ')
    roll_no = StringField('Student Roll No : ')
    submit = SubmitField('Add Student')

class DeleteForm(FlaskForm):
    id = IntegerField('Roll No of Student to delete : ')
    submit = SubmitField('Delete Student')