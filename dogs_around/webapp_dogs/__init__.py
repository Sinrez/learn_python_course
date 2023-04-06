# source env_dogs/bin/activate
# ./run.sh

from webapp_dogs.forms import LoginForm
from flask import Flask, render_template, flash, redirect, url_for
# from webapp_dogs.model  import db
from flask_migrate import Migrate
import datetime
from wtforms.validators import DataRequired, Length, ValidationError
from flask_wtf import FlaskForm, csrf
from wtforms import StringField, SubmitField
from webapp_dogs import config


app = Flask(__name__)
app.secret_key = config.SECRET_KEY

@app.route("/")
def index():
    title = 'Собакруг'
    return render_template('index.html', page_title=title)


@app.route('/login')
def login():
    title = "Авторизация"
    login_form = LoginForm()
    return render_template('login.html', page_title=title, form=login_form)

@app.route('/register')
def register():
    pass

@app.route('/register/dog')
def register():
    pass