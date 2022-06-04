from flask import redirect, url_for, flash
from flask_login import current_user
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView

from app import db
from app.models import User, Item


class MyModelView(ModelView):
    can_export = True
    export_types = ['xlsx']
    page_size = 1000

    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        flash('管理者ユーザーにログインしてください。', category='error')
        return redirect(url_for('auth.login'))


class MyUserView(ModelView):
    can_create = False
    can_edit = False
    can_export = True
    export_types = ['xlsx']

    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        flash('管理者ユーザーにログインしてください。', category='error')
        return redirect(url_for('auth.login'))


class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        flash('管理者ユーザーにログインしてください。', category='error')
        return redirect(url_for('auth.login'))


def setup_admin(app):
    admin = Admin(app, index_view=MyAdminIndexView())

    admin.add_view(MyUserView(User, db.session))
    admin.add_view(MyModelView(Item, db.session))
