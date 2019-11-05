from app import app, db
from flask import render_template, url_for, redirect, flash, jsonify, request
from app.forms import LoginForm, CustomerForm, MaintenanceForm
from app.models import Staff, Inventory, Car
from flask_login import login_user, logout_user, login_required, current_user
import datetime


@app.route('/')
@app.route('/index', methods=['GET'])
def index():

    inventory = db.session.execute('''
    SELECT make, model, year, price FROM inventory
    INNER JOIN car on (inventory.car_id) = (car.car_id)
    ''')

    return render_template('index.html', title='Home', inventory=inventory)


@app.route('/customers', methods=['GET', 'POST'])
def customers():
    form = CustomerForm()

    if form.validate_on_submit():
        full_name = form.first_name.data.title() + ' ' + form.last_name.data.title()

        cars = db.session.execute('''
        SELECT full_name, make, model, year, color FROM car
        INNER JOIN customer ON car.cust_id = customer.cust_id
        WHERE customer.full_name = '{}'
        '''.format(full_name))

        return render_template('form.html', title='Customers', form=form, cars=cars)

    return render_template('form.html', title='Customers', form=form)


@app.route('/maintenance', methods=['GET', 'POST'])
def maintenance():

    if not current_user:
        return redirect(url_for('index'))

    form = MaintenanceForm()

    if form.validate_on_submit():
        staff_id = current_user.staff_id
        payment_id = form.payemnt_id.data
        start_date = form.start_date.data
        end_date = form.end_date.data
        description = form.description.data
        maintenance = Maintenance(staff_id=current_user.staff_id, payment_id=payment_id, start_date=start_date, end_date=end_date, description=description)

        db.session.add(maintenance)
        db.session.commit()

        return render_template('form.html', title='Maintenance', form=form)

    return render_template('form.html', title='Maintenance', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    # if user is already logged in, redirect them
    if current_user.is_authenticated:
        flash('You are already logged in!')
        return redirect(url_for('index'))

    form = LoginForm()

    if form.validate_on_submit():
        # query db for user info, and log them in if everything is valid
        staff = Staff.query.filter_by(staff_id=form.staff_id.data).first()

        # if user doesn't exist, reload page and flash message
        if user is None or not user.check_password(form.password.data):
            flash('Invalid Credentials.')
            return redirect(url_for('login'))

        # if user does exist, and credentials are valid
        login_user(user)
        flash('You have been logged in!')
        return redirect(url_for('index'))

    return render_template('form.html', form=form, title='Login')
