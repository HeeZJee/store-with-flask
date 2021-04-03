from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField


class RegisterForm(FlaskForm):
        
    username= StringField(label='User Name')
    email= StringField(label='Email Address')
    password= PasswordField(label='Password')
    password_confirm= PasswordField(label='Confirm Password')
    submit= SubmitField(label='Create Account')
