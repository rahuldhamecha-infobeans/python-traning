from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Go To Puppy_name/name and see the result!</h1>'

@app.route('/puppy_name/<name>')
def puppy_latin(name):
    pup_name = ''
    if name[-1] == 'y':
        pup_name = name[:-1] + 'iful'
    else:
        pup_name = name + 'y'

    return '<h1> Puppy Name : {}'.format(pup_name)

if __name__ == '__main__':
    app.run()