from flask_login import UserMixin
from werkzeug.security import generate_password_hash

from app import db


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255))
    name = db.Column(db.String(20), nullable=False)

    def __init__(self, id=None, email=None, password=None, name=None):
        self.id = id
        self.email = email
        self.name = name
        self.password = generate_password_hash(password)
