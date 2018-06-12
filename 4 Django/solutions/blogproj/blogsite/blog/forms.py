from django import forms 
from .models import BlogPost, Comment

class BlogPostForm(forms.Form):
    # class Meta:
    #     # the model to associate with the form
    #     model = BlogPost
    #     # a list of all the models' fields you want in the form
    #     fields = ['title', 'body']
    title = forms.CharField(label='Title', max_length=100)
    body = forms.CharField(label='Body')

class CommentForm(forms.Form):
    comment_body = forms.CharField(label='Comment', max_length=500)