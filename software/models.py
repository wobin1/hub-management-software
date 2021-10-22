from . import db
from flask_login import UserMixin



# app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:password@localhost:5432/hub_db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db=SQLAlchemy(app)
# migrate = Migrate(app, db)

class Super_admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))
    password = db.Column(db.String(20), nullable=False)

class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phonenumber = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)


