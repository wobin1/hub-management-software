from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from .models import Admin, Subscriber
from . import db
import qrcode
from PIL import Image
import os

views = Blueprint('views', __name__)

# Subscriber view
@views.route('/')
@login_required
def index():
    subscribers = Subscriber.query.all()
    context = {
        'subscriber': subscribers,
        'users': current_user
    }
    
    return render_template('index.html', subscribers=subscribers, user=current_user )

# subscriber detail view
@views.route('/subscriber_detail/<int:id>', methods=["GET", "POST"])
def subscriber_detail(id):
    query = Subscriber.query.get_or_404(id)
    return render_template('subscriber_detail.html', user=current_user, subscriber=query)

@views.route('/subscriber_update/<int:id>', methods=["POST", "GET"])
def subscriber_update(id):
    sub_update = Subscriber.query.get_or_404(id)
    if request.method == "POST":
        sub_update.sub_firstname = request.form.get('sub_firstname')
        sub_update.sub_surname = request.form.get('sub_surname')
        sub_update.sub_email = request.form.get('sub_email')
        sub_update.sub_phonenumber = request.form.get('sub_phonenumber')
        sub_update.sub_address = request.form.get('sub_address')


        db.session.commit()
        return redirect('/')

        return "there was a problem editing subscriber's details please try again"
    else:
        return render_template('subscriber_update.html', user=current_user, sub = sub_update)

# Delete Subscribers
@views.route('/subscriber_delete/<int:id>')
def subscriber_delete(id):
    sub_delete= Subscriber.query.get_or_404(id)
    try:
        db.session.delete(sub_delete)
        db.session.commit()
        return redirect('/')
    except:
        return "there was a problem deleting your item "


# Generate Id
@views.route('/generate_id/<int:id>')
def generate_id(id):
    query = Subscriber.query.get_or_404(id)

    
    return render_template('id_card.html', user=current_user, sub=query)

@views.route('/admin_detail')
def admin_detail():
    return render_template('admin_detail.html')


@views.route('/generate_qr/<int:id>')
def generate_qr(id):
    user = Subscriber.query.get_or_404(id)

    img = qrcode.make(f"{user.id}")
    path = 'software/static/qrcode/subscribers'
    imagepath = os.path.join(path, f"{user.id}.jpg")
    img.save(imagepath)    
    return "QR generated sucessfully!!!!!"

