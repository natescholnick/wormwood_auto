from app import app, db
from app.models import Maintenance, Staff, Customer, Car
from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, IntegerField, DateTimeField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError


class LoginForm(FlaskForm):
    staff_id = IntegerField('Staff ID #', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class CustomerForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(max=29)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(max=50)])
    submit = SubmitField('Find Customer')

class MaintenanceForm(FlaskForm):
    payment_id = IntegerField('Payment ID #', validators=[DataRequired()])
    start_date = DateTimeField('Start Date', validators=[DataRequired()])
    end_date = DateTimeField('End Date', validators=[DataRequired()])
    description = TextAreaField('What maintenance was performed?', validators=[DataRequired()])
    submit = SubmitField('Add Record')
