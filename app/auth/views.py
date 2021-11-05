from flask import render_template, redirect,url_for,request,flash
from . import auth
from ..models import User
from .forms import  RegistrationForm, LoginForm



@auth.route('/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    # if request.method == 'POST':
    #     if login_form.validate_on_submit():
    #         user = User.query.filter_by(email = login_form.email.data).first()
    #         if user is not None and user.verify_password(login_form.password.data):
    #             login_user(user,login_form.remember.data)
    #             return redirect(request.args.get('next') or url_for('main.index'))

    #         flash('Invalid username or Password')

    return render_template('login.html',form = login_form)


@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User(name= form.name.data,email = form.email.data, username = form.username.data, password = form.password.data)
            user.save_user()
            flash('Registered successfully')
            return redirect(url_for('auth.login'))
    return render_template('register.html', form = form)


#@auth.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for("main.index"))


