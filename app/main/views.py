from flask import render_template,url_for,request,flash,redirect,abort
from . import main
from .forms import  PitchForm,CommentForm
from ..models import Pitch,User,Comment
from flask_login import login_required,current_user



@main.route('/')
@main.route('/home')
def index():
    pitches = Pitch.query.all()
    if pitches is None:
        abort(404)
    return render_template('home.html', pitches = pitches)


@main.route('/<category>',methods=['POST','GET'])
def pitch_category(category):
    pitches = Pitch.query.filter_by(category = category).all()
    if pitches is None:
        abort(404)
    return render_template('category.html', pitches = pitches)



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


@main.route('/profile', methods = ['GET','POST'])
@login_required
def profile():
    return render_template('profile.html',user = current_user)


@main.route('/<post_id>/comment', methods = ['GET','POST'])
@login_required
def comment_post(post_id):
    form = CommentForm()
    pitch = Pitch.query.filter_by(id = post_id).first()
    if pitch is None:
        abort(404)
        
    if request.method == 'POST':
        if form.validate_on_submit():
            new_comment = Comment( content=form.comment.data, pitch_id = post_id, user_id = current_user.id)
            new_comment.save_comment()
            flash('Comment posted!')
            return redirect(url_for('main.comment_post', post_id=post_id))
    
    return render_template('comment.html',form=form, pitch = pitch)

