from . import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(10))
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(100))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")



    def __repr__(self):
        return f'User {self.name}'


class Quote():
    '''
    class to define quote objects
    '''
    def __init__(self,author,id,quote):
        self.author=author
        self.id = id
        self.quote = quote
        self.permalink = permalink

class Blog(db.Model):
    __tablename__ = 'blog'
    """
    Class to define blog objects
    """
    id = db.Column(db.Integer,primary_key = True)
    author=db.Column(db.String(100))
    title=db.Column(db.String(100))
    description=db.Column(db.String(1000))
    category=db.Column(db.String(), nullable=False)
    pic_path=db.Column(db.String(1000))
    url=db.Column(db.String(10000))

    @classmethod
    def get_blogs(cls, category):
        blogs = Blog.query.order_by(blog_category=category).desc().all()
        return blogs

    def __repr__(self):
        return f'Blog{self.description}'

class Subscribe(db.Model):
    __tablename__= 'subscribers'
    all_subscribe=[]
    '''
    class to define subscribers objects
    '''
    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String(255),unique = True,index = True)

class Fashion:
    fashion=[]
    def __init__(self,title,description):
        self.title = title
        self.description = description
class Food:
    food=[]
    def __init__(self,title,description):
        self.title = title
        self.description = description

class Life:
    product=[]
    def __init__(self,title,description):
        self.title = title
        self.description = description

class Fitness:
    interview=[]
    def __init__(self,title,description):
        self.title = title
        self.description = description


    # def save_subscribe(self):
    #     Subscribe.all_subscribe.append(self)
    #
    #
    # @classmethod
    # def clear_reviews(cls):
    #     Subscribe.all_subscribe.clear()
