from flask import Blueprint, render_template
from sqlalchemy import desc

from app.models import Item, NavLink

main = Blueprint('main', __name__, static_folder='static')


@main.route('/')
def home() -> str:
    items = Item.query.order_by(desc(Item.id)).all()
    nav_links = NavLink.query.order_by(NavLink.left_num).all()
    return render_template(
        "./main/top_page.html", items=items, nav_links=nav_links)
