from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired
from sqlalchemy import Column, Integer, String
from application import Base

class User(Base):
        __tablename__ = 'users'
        id = Column(Integer, primary_key=True)
        name = Column(String(50), unique=True)
        password = Column(String(120))

class RegistrationForm(FlaskForm):
        username = StringField('username')
        password = PasswordField('password')
        submit = SubmitField('submit')

class SigninForm(FlaskForm):
        username = StringField('username', validators=[DataRequired()])
        password = PasswordField('password', validators=[DataRequired()])
        submit = SubmitField('sign-In')
        remember = BooleanField('remember me?')