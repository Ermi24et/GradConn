from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, TextAreaField, SelectField, DateField
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

class JobForm(FlaskForm):
    position_title = StringField('Position Title', validators=[InputRequired()])
    contract_type = StringField('Contract Type', validators=[InputRequired()])
    working_condition = SelectField('Working Condition', choices=[('Remote', 'Remote'), ('Hybrid', 'Hybrid'), ('On Site', 'On Site')], validators=[InputRequired()])
    type_of_vacancy = SelectField('Type of Vacancy', choices=[('Volunteer', 'Volunteer'), ('Internship', 'Internship'), ('Fellowship', 'Fellowship')], validators=[InputRequired()])
    organization_description = TextAreaField('Organization Description', validators=[InputRequired()])
    job_description = TextAreaField('Job Description', validators=[InputRequired])
    required_education_experience = TextAreaField('Required Education & Experience', validators=[InputRequired()])
    skills = TextAreaField('Skills', validators=[InputRequired()])
    how_to_apply = TextAreaField('How to Apply', validators=[InputRequired()])
    disclaimer = TextAreaField('Disclaimer', validators=[InputRequired()])
    deadline_date = DateField('Application Deadline', format='%Y-%m-%d', validators=[InputRequired()])
    submit = SubmitField('Post Job')
