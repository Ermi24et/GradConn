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

class JobForm(FlaskForm):
    position_title = StringField('Position Title', validators=[DataRequired()])
    contract_type = StringField('Contract Type', validators=[DataRequired()])
    working_condition = SelectField('Working Condition', choices=[('Remote', 'Remote'), ('Hybrid', 'Hybrid'), ('On Site', 'On Site')], validators=[DataRequired()])
    type_of_vacancy = SelectField('Type of Vacancy', choices=[('Volunteer', 'Volunteer'), ('Internship', 'Internship'), ('Fellowship', 'Fellowship')], validators=[DataRequired()])
    organization_description = TextAreaField('Organization Description', validators=[DataRequired()])
    job_description = TextAreaField('Job Description', validators=[DataRequired])
    required_education_experience = TextAreaField('Required Education & Experience', validators=[DataRequired()])
    skills = TextAreaField('Skills', validators=[DataRequired()])
    how_to_apply = TextAreaField('How to Apply', validators=[DataRequired()])
    disclaimer = TextAreaField('Disclaimer', validators=[DataRequired()])
    deadline_date = DateField('Application Deadline', format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField('Post Job')
