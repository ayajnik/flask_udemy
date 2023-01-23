import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

login_manager = LoginManager()

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.getcwd() +'/'+ 'data.sqlite'
print('\n')
print(app.config['SQLALCHEMY_DATABASE_URI'])
print('\n')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Migrate(app,db)
## setting up login manager to our application
login_manager.init_app(app)
## routing login manager to the view
login_manager.login_view='login'



