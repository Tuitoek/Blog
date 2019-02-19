from flask import render_template,redirect,url_for,flash,request
from ..models import User
from .forms import RegisterForm,LoginForm
from flask_login import login_user,logout_user,login_required
from .. import db
from . import auth
# from ..email import mail_message


@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()

        # mail_message("Welcome to Tuitoek's blog","email/welcome_user",user.email,user= user)
        return redirect(url_for('auth.login'))
        title = "New Account"
        flash("A signup email has been sent to your account")
    return render_template('auth/signup.html',register_form = form)

@auth.route('/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or Password')

    return render_template('auth/login.html',login_form = login_form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))

