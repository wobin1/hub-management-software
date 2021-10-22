from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)


@views.route('/')
@login_required
def index():
    return render_template('index.html', user=current_user)

@views.route('/subscriber_detail')
def subscriber_detail():
    return render_template('subscriber_detail.html')

@views.route('/subscribers_with_balance')
def subscribers_with_balance():
    return render_template('pending_ballance.html')

@views.route('/admin_detail')
def admin_detail():
    return render_template('admin_detail.html')


@views.route('/gerate_id')
def gerate_id():
    return render_template('generate_id.html')