import os

from flask import Blueprint, url_for, redirect, render_template


main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
def home():
    return render_template('main/home.html', title='Home')
