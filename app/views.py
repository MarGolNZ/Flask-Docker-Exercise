from flask import render_template
from app import app


@app.route('/')
def home():
    return "hello world 2!"


@app.route('/template')
def template():
    return render_template('home.html')
