from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import Required,Email,EqualTo
from wtforms import ValidationError
from  ..models import User

#Registration Form
class RegistrationForm(FlaskForm):
    name = StringField('Your name:',validators=[Required()])
    email = StringField('Your Email Address:',validators=[Required(),Email()])
    username = StringField('Enter your username:',validators = [Required()])
    password = PasswordField('Password:',validators = [Required(), EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Password:',validators = [Required()])
    submit = SubmitField('Sign Up')
    
    
    def validate_email(self,data_field):
        if User.query.filter_by(email =data_field.data).first():
            flash('There is an account with that email','danger')
            raise ValidationError('There is an account with that email')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            flash('That username is taken','danger')
            raise ValidationError('That username is taken')
        
        
        
#Login Form     
class LoginForm(FlaskForm):
    email = StringField('Your Email Address:',validators=[Required(),Email()])
    password = PasswordField('Password:',validators =[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')