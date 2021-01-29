from django.forms import ModelForm
from post.models import Post, Comment,Reply


class PostCreateForm(ModelForm):
    class Meta:
        model=Post
        fields=[
             'title','text','tag',
        ]

class CommentForm(ModelForm):
    class Meta:
        model=Comment
        fields=[
            'text'
        ]

class ReplyForm(ModelForm):
    class Meta:
        model=Reply
        fields=[
            'text'
        ]
