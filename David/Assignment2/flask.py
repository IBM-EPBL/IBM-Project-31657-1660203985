from flask import Flask;
from flask import render_template;

app = Flask(_name_)

@app.route("/")
def home():
    return render_template('login.html')

@app.route('/signup')
def show():
    return render_template('registerpg.html')