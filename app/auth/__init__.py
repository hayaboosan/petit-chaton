from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import logout_user, login_required

from app import db
from app.models.auth import User
from app.forms.auth import LoginForm, CreateUserForm


auth = Blueprint('auth', __name__)


@auth.route('/')
@login_required
def index():
    return render_template('./auth/index.html')


@auth.route('/login', methods=['GET', 'POST'])
def login() -> str:
    create_first()
    form = LoginForm()
    if form.validate_on_submit():
        return form.validate_login()
    return render_template("./auth/login.html", form=form)


def create_first():
    if len(User.query.all()) == 0:
        db.session.add(User(
            email='admin@example.com', name='admin',
            password='password'))
    db.session.commit()


@auth.route('/create', methods=['POST', 'GET'])
@login_required
def create() -> str:
    form = CreateUserForm()
    if form.validate_on_submit():
        return form.validate_user()
    return render_template('./auth/create.html', form=form)


@auth.route('/logout')
@login_required
def logout() -> str:
    logout_user()
    flash('ログアウトしました', category='success')
    return redirect(url_for('auth.login'))
