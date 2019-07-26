import os
from flask import Flask, session, render_template, url_for, redirect, request, flash
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from forms import SigninForm, RegistrationForm, User
from flask_wtf import FlaskForm

#instantiate app
app = Flask(__name__)

# Check for database variable and if it is not there, returns an error
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# secret key is for WTForms
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

# something to do with sessions
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

# set app to use database
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# connect to database
engine = create_engine(os.getenv("DATABASE_URL"))
#db_session = scoped_session(sessionmaker(bind=engine))

#Base = declarative_base()
#Base.query = db_session.query_property()
#7.26 -- db_session.add() --add isn't part of >>scoped_session(sessionmaker)

Session(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signin")
def signin():
    #adding form to route
    form = SigninForm()
    # passing form to template        
    return render_template("signin.html", form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    # adding form to route
        # different option: res = request.form.get("id")
    form = RegistrationForm()
    #add user info to database
    if form.validate_on_submit():
        return redirect('/search')

    #if request.method == 'POST' and form.valiate():
        #user = User(form.username.data, form.password.data)
        #db_session.add(user)
        #flash('Thanks for registering')
    return render_template("register.html", form=form)

@app.route("/search")
def search():
    return render_template("search.html")