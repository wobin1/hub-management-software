from . import db
from flask_login import UserMixin



# app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:password@localhost:5432/hub_db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db=SQLAlchemy(app)
# migrate = Migrate(app, db)

class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phonenumber = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"{self.firstname}"

class Subscriber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phonenumber = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(100), nullable=False)

    def __str__(self):
        return f"{self.id}, {self.firstname}"




