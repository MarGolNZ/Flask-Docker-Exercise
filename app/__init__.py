from flask import Flask
from app import views

app = Flask('test', template_folder='./templates/')
