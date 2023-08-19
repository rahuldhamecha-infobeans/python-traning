from flask import Flask, render_template,request,session,redirect,url_for,flash
from flask_wtf import FlaskForm
from wtforms import (StringField,SubmitField,BooleanField,DateTimeField,SelectField, RadioField)
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecrete_key'

@app.route('/') # 127.0.0.1:5000
def index():
    return render_template('index.html')

@app.route('/information') # 127.0.0.1:5000
def info():
    return render_template('information.html')

@app.route('/info/<name>')
def dynamic_info(name):
    return "My Name is : {}".format(name.upper())

@app.route('/basic-template')
def basic_template():
    name = "Darsh Shah"
    letters = list(name)
    user_logged_in = True
    return render_template('basic.html',my_name=name,letters=letters,user_logged_in=user_logged_in)

@app.route('/forms')
def forms():
    return render_template('forms.html')

@app.route('/thank_you')
def thank_you():
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')
    return render_template('thank_you_form.html',first_name=first_name,last_name=last_name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

class InfoForm(FlaskForm):

    name = StringField("What's your name?",validators=[DataRequired()])
    submit = SubmitField('Submit')

    
@app.route('/flask-form-basic', methods=['GET', 'POST'])
def flask_form_basic():

    name = False
    form = InfoForm()

    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash("Your Name is  : {}".format(name))
        # session['name_demo'] = name

        # return redirect(url_for('thank_you'))

    return render_template('flask-form.html',form=form,name=name)

if __name__ == '__main__':
    app.run(debug=True)