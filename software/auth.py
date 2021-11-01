from flask import Blueprint,render_template, request, flash, redirect, url_for
from . import db
import werkzeug
from .models import Admin, Subscriber
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth= Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        email = email


        user = Admin.query.filter_by(email=email).first()
    

        print(password)
        print(email)
        if user:
            if check_password_hash(user.password, password):
                flash('logged in successfully!!!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.index'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('User does not exist', category='error')           

    return render_template('login.html', user=current_user)

@auth.route('/create_user', methods=['GET', 'POST'])
def create_user():
    if request.method == "POST":
        firstname = request.form.get('firstname')
        surname = request.form.get('surname')
        email = request.form.get('email')
        phonenumber = request.form.get('phonenumber')
        address = request.form.get('address')
        role = request.form.get('role')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        print(firstname)
        print(surname)
        print(len(email))

        user = Admin.query.filter_by(email=email).first()
        if user:
            flash("user already exit", category='error')
        elif len(email) < 1:
            flash("Email field can not be empty", category= 'error')
        elif len(firstname) < 1:
            flash("first Name field can not be empty", category= 'error')
        elif len(surname) < 1:
            flash("Surname field can not be empty", category= 'error')
        elif len(phonenumber) < 11:
            flash("phone number must be upto 11 digits", category= 'error')
        elif len(phonenumber) > 14:
            flash("phone number must not be more than 11 digits", category= 'error')
        elif len(address) < 1:
            flash("please address must be more than one character", category= 'error')
        elif len(role) < 1:
            flash("please role must be more than one character", category= 'error')
        elif password1 != password2:
            flash("password did not match", category= 'error')
        elif len(password1) < 7:
            flash("password must be greater than 7 characters")
        else:
            new_user = Admin(firstname=firstname, surname=surname, email=email, phonenumber=phonenumber, address=address, role=role, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash("Account created !!!!", category= 'success')
        return redirect(url_for('views.index'))
    return render_template('create_user.html', user=current_user)



@auth.route('/create_subscriber', methods=['GET', 'POST'])
def create_subscriber():

    if request.method=='POST':
        firstname = request.form.get('sub_firstname')
        surname = request.form.get('sub_surname')
        email = request.form.get('sub_email')
        phone = request.form.get('sub_phonenumber')
        address = request.form.get('sub_address')

        print(firstname)
        print(surname)
        print(email)
        print(phone)
        print(address)

        user_email = Subscriber.query.filter_by(email=email).first()

        if user_email:
            flash('subscriber already exist', category='error')
        elif len(email) < 1:
            flash('email field can not be empty', category='error')
        elif len(firstname) < 1:
            flash('name field can not be empty', category='error')
        elif len(surname) < 1:
            flash('surname field can not be empty', category='error')
        elif len(phone) < 11:
            flash('phone number can not be less than 11 digit', category='error')
        elif len(phone) > 14:
            flash('phone number can not be less than 11 digit', category='error')
        elif len(address) < 1:
            flash('address field can not be empty', category='error')
        else:
            new_subscriber= Subscriber(firstname=firstname, surname=surname, email=email, phonenumber=phone, address=address)
            db.session.add(new_subscriber)
            db.session.commit()
            flash('Subscriber added succesfully', category='success')
    return render_template('create_subscriber.html', user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
