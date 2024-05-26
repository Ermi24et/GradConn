from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, TextAreaField, SelectField
from wtforms.validators import Length, EqualTo, Email, InputRequired, ValidationError


class SignUpForm(FlaskForm):
    first_name = StringField('First Name', validators=[Length(min=3, max=30), InputRequired()])
    last_name = StringField('Last Name', validators=[Length(min=3, max=30), InputRequired()])
    email = StringField('Email', validators=[Email(), InputRequired()])
    password = PasswordField('Password', validators=[Length(min=6), InputRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[EqualTo('password'), InputRequired()])
    submit = SubmitField('Sign Up')

class SignInForm(FlaskForm):
    email = StringField('Email', validators=[Email(), InputRequired()])
    password = PasswordField('Password', validators=[Length(min=6), InputRequired()])
    submit = SubmitField('Sign In')

class AdminSignUpForm(FlaskForm):
    name = StringField('Organization Name', validators=[Length(min=3, max=30), InputRequired()])
    email = StringField('Email', validators=[Email(), InputRequired()])
    password = PasswordField('Password', validators=[Length(min=6), InputRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[EqualTo('password'), InputRequired()])
    submit = SubmitField('Sign Up')

class AdminSignInForm(FlaskForm):
    email = StringField('Email', validators=[Email(), InputRequired()])
    password = PasswordField('Password', validators=[Length(min=6), InputRequired()])
    submit = SubmitField('Sign In')