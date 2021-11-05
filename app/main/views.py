from flask import render_template,url_for
from . import main
from flask_login import login_required



@main.route('/')
@main.route('/home')
def index():
    return render_template('home.html')