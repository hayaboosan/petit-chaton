from flask import Blueprint, render_template, redirect, url_for

main = Blueprint('main', __name__, static_folder='static')


@main.route('/')
def home() -> str:
    return render_template("./main/top_page.html")
