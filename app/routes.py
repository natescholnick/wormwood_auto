from app import app, db
from flask import render_template, url_for, redirect, flash, jsonify, request
from app.forms import LoginForm, CustomerForm, MaintenanceForm
from app.models import Staff, Inventory, Car
from flask_login import login_user, logout_user, login_required, current_user
import datetime


@app.route('/')
@app.route('/index')
def index():

    inventory = Inventory.query.all()

    return render_template('index.html', title='Home', inventory=inventory)


@app.route('/customers', methods=['GET', 'POST'])
def customers():
    form = CustomerForm()

    return render_template('form.html', title='Customers', form=form)


@app.route('/maintenance', methods=['GET', 'POST'])
def maintenance():
    form = MaintenanceForm()

    return render_template('form.html', title='Maintenance', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    # if user is already logged in, redirect them
    if current_user.is_authenticated:
        flash('You are already logged in!')
        return redirect(url_for('profile', username=current_user.username))

    form = LoginForm()

    if form.validate_on_submit():
        # query db for user info, and log them in if everything is valid
        user = User.query.filter_by(email=form.email.data).first()

        # if user doesn't exist, reload page and flash message
        if user is None or not user.check_password(form.password.data):
            flash('Invalid Credentials.')
            return redirect(url_for('login'))

        # if user does exist, and credentials are valid
        login_user(user)
        flash('You have been logged in!')
        return redirect(url_for('profile', username=current_user.username))

    return render_template('form.html', form=form, title='Login')
