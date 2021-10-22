from flask import Blueprint,render_template, request, flash, redirect, url_for
from . import db
import werkzeug
from .models import Admin, Super_admin
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
            flash('email does not exist', category='error')           

    return render_template('login.html', user=current_user)

@auth.route('/create_admin', methods=['GET', 'POST'])
def create_admin():
    if request.method == "POST":
        firstname = request.form.get('firstname')
        surname = request.form.get('surname')
        email = request.form.get('email')
        phonenumber = request.form.get('phonenumber')
        address = request.form.get('address')
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
            flash("please email must be more than one character", category= 'error')
        elif password1 != password2:
            flash("password did not match", category= 'error')
        elif len(password1) < 7:
            flash("password must be greater than 7 characters")
        else:
            new_admin = Admin(firstname=firstname, surname=surname, email=email, phonenumber=phonenumber, address=address, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_admin)
            db.session.commit()
            flash("Account created !!!!", category= 'success')
            return redirect(url_for('views.index'))

    return render_template('create_admin.html')

@auth.route('/create_subscriber')
def create_subscriber():
    return render_template('create_subscriber.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
