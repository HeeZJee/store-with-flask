from src.models import User
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError



class RegisterForm(FlaskForm):
    def validate_username(self, username_to_validate):
        user = User.query.filter_by(username=username_to_validate.data).first()
        if user:
            raise ValidationError("Username already Exist! please try a different username.")
    
    def validate_email(self, email_to_validate):
        user = User.query.filter_by(email=email_to_validate.data).first()
        if user:
            raise ValidationError("Email already Exist! please try a different email address.")

    username = StringField(label='User Name', validators=[Length(min=3, max=30), DataRequired()])
    email= StringField(label='Email Address', validators=[Email(), DataRequired()])
    password= PasswordField(label='Password',validators=[Length(min=6), DataRequired()])
    password_confirm= PasswordField(label='Confirm Password',validators=[EqualTo('password') , DataRequired()])
    submit= SubmitField(label='Create Account')
