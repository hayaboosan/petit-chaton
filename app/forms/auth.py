from flask_wtf import FlaskForm
from flask import flash, render_template, redirect, url_for
from flask_login import login_user
from wtforms import (
    SubmitField, PasswordField, EmailField,
    StringField, BooleanField, SelectField)
from wtforms.validators import InputRequired, Email, Length
from werkzeug.security import check_password_hash, generate_password_hash

from app.models.auth import User
from app import db


class LoginForm(FlaskForm):
    email = EmailField('メールアドレス', validators=[
        InputRequired('必須です')])

    password = PasswordField('パスワード')

    submit = SubmitField()

    def validate_login(self):
        user = self.get_user_email()
        if user is None or \
                not check_password_hash(user.password, self.password.data):
            flash('ログイン情報を確認してください', category='error')
            return redirect(url_for('auth.login'))
        login_user(user, remember=True)
        return 'ログインしました。'

    def get_user_email(self):
        return User.query.filter_by(email=self.email.data).first()
