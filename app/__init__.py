from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from sqlalchemy.orm import scoped_session, sessionmaker
import os


from config import DATABASE_URI, engine


def import_blueprint(app):
    @app.route('/')
    def home():
        return redirect(url_for('auth.login'))

    from app.auth import auth
    app.register_blueprint(auth, url_prefix='/auth')


def options(app):
    from flask_bootstrap import Bootstrap
    Bootstrap(app)

    from flask_migrate import Migrate
    return Migrate(app, db)


db = SQLAlchemy()
session = scoped_session(sessionmaker(
    autocommit=False, autoflush=False, bind=engine))

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
db.create_all(app=app)
migrate = options(app)

import_blueprint(app)
