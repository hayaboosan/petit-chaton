from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import logout_user, login_required
from app.forms.auth import LoginForm


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login() -> str:
    form = LoginForm()
    if form.validate_on_submit():
        return form.validate_login()
    return render_template("./auth/login.html", form=form)
