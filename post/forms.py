from django.forms import ModelForm
from post.models import Post


class PostCreateForm(ModelForm):
    class Meta:
        model=Post
        fields=[
             'title','text',
        ]
