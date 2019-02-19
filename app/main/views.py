from flask import render_template,request,redirect,url_for,abort
from ..models import Subscribe,User,Blog
from . import main
from .forms import SubscribeForm,UpdateProfile,BlogForm
from flask_login import login_required
from .. import db,photos
import requests
import json


# Views
@main.route('/',methods= ['POST', 'GET'])
def index():
    subscribe_form = SubscribeForm()
    '''
    View root page function that returns the index page and its data
    '''
    if subscribe_form.validate_on_submit():
        email = subscribe_form.email.data
        # new_subscribe = Subscribe(email)
    title="Tuitoek's blog"

    display = requests.get('http://quotes.stormconsultancy.co.uk/random.json').json()

    return render_template('index.html',title = title,subscribe_form =subscribe_form,display = display,blog=Blog.query.all())

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update/pic',methods= ['POST','GET'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
        return redirect(url_for('.profile',uname=user.username))
    return redirect(url_for('main.update_pic',uname=uname))

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data
        user.profile_pic_path = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/fashion', methods=['GET', 'POST'])
def fashion():
    blog = Blog.query.filter_by().first()
    Fashionblog = Blog.query.filter_by(category="Fashionblog")
    return render_template('blogs.html', blog=blog, fashionblog=fashionblog)

@main.route('/food', methods=['GET', 'POST'])
def fashpromotionpitchion():
    blog = Blog.query.filter_by().first()
    Foodblog = Blog.query.filter_by(category="Foodblog")
    return render_template('blogs.html', blog=blog, foodblog=foodblog)

@main.route('/life', methods=['GET', 'POST'])
def life():
    blog = Blog.query.filter_by().first()
    Lifeblog = Blog.query.filter_by(category="lifeblog")
    return render_template('blogs.html', blog=blog, lifeblog=lifeblog)

@main.route('/fitness', methods=['GET', 'POST'])
def fitness():
    blog = Blog.query.filter_by().first()
    fitnessblog = Blog.query.filter_by(category="Fitnessblog")

    return render_template('blogs.html', blog=blog,fitnessblog = fitnessblog)

@main.route('/blog',methods=['GET','POST'])
def post_blog():
    blog_form = BlogForm()

    if blog_form.validate_on_submit():
        title = blog_form.title.data
        description = blog_form.description.data
        category=blog_form.category.data
        post_blog = Blog(title=title,description=description,category=category)

        db.session.add(post_blog)
        db.session.commit()

        return redirect(url_for('main.index'))

    return render_template('blogs.html',blog_form=blog_form)
