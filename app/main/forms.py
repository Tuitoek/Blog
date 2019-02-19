from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,RadioField, SelectField
from wtforms.validators import Required,Length

class SubscribeForm(FlaskForm):
    email = TextAreaField('Enter your emailadress to subscribe to the blog site',validators=[Required()])
    submit = SubmitField('Click to subscribe',validators=[Required()])

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class BlogForm(FlaskForm):
    title=StringField('Enter your title',validators = [Required()])
    description = TextAreaField("Write your blog",validators=[Required()])
    category = SelectField('Select category',choices=[('Fashionblog', 'Fashion'), ('Fitnessblog' ,'Fitness'), ('Foodblog','Food'), ('Lifebloglog','Life')])
    submit = SubmitField("Post Blog",validators=[Required()])
