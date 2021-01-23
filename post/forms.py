from django.forms import ModelForm
from post.models import Post, Comment


class PostCreateForm(ModelForm):
    class Meta:
        model=Post
        fields=[
             'title','text',
        ]

class CommentForm(ModelForm):
    class Meta:
        model=Comment
        fields=[
            'text'
        ]
