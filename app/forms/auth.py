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
    email = EmailField('メールアドレス', validators=[InputRequired('必須です')])

    password = PasswordField('パスワード')

    submit = SubmitField()

    def validate_login(self):
        user = User.query.filter_by(email=self.email.data).first()
        if user is None or \
                not check_password_hash(user.password, self.password.data):
            flash('ログイン情報を確認してください', category='error')
            return redirect(url_for('auth.login'))
        login_user(user, remember=True)
        return redirect(url_for('admin.index'))


class CreateUserForm(FlaskForm):
    email = EmailField('メールアドレス', validators=[
        InputRequired('必須です'),
        Email(message='有効なメールアドレスではありません')])

    name = StringField('ユーザー名', validators=[
        InputRequired('必須です'),
        Length(max=20, message='20文字以内で入力してください')])

    password = PasswordField('パスワード', validators=[
        InputRequired('必須です')])

    submit = SubmitField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def validate_user(self):
        is_registered = User.query.filter_by(email=self.email.data).first()
        if is_registered is not None:
            flash('メールアドレスが既に存在します。', category='error')
            return render_template('./auth/create.html', form=self)

        user = User(
            email=self.email.data, name=self.name.data,
            password=self.password.data)
        db.session.add(user)
        db.session.commit()
        return 'ユーザーを作成しました。'
