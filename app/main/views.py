from flask import render_template,url_for,request,flash,redirect
from . import main
from .forms import  PitchForm
from ..models import Pitch
from flask_login import login_required,current_user



@main.route('/')
@main.route('/home')
def index():
    return render_template('home.html')

@main.route('/add-pitch', methods = ['GET','POST'])
@login_required
def add_pitch():
    form = PitchForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            new_pitch = Pitch( category=form.category.data, content=form.content.data, user_id = current_user.id)
            new_pitch.save_pitch()
            flash('pitch posted!')
            return redirect(url_for('main.index'))
            
    return render_template('addpitch.html', form=form)