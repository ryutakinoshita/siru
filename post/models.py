from django.db import models
from accounts.models import User
from django.utils import timezone


class Post(models.Model):
    author=models.ForeignKey(User,verbose_name='ユーザー',on_delete=models.SET_DEFAULT,default='退会済みのユーザー')
    title=models.CharField(max_length=100,verbose_name='タイトル',blank=False,null=False)
    text=models.TextField(max_length=2000,verbose_name='テキスト',blank=False,null=False)
    time=models.DateTimeField(verbose_name='投稿日',default=timezone.now)

    def __str__(self):
        return self.title


class Comment(models.Model):
    target=models.ForeignKey(Post,verbose_name='該当の投稿',on_delete=models.CASCADE)
    author=models.ForeignKey(User,verbose_name='ユーザー',on_delete=models.SET_DEFAULT,default='退会済みのユーザー')
    text=models.TextField(verbose_name='コメント')
    time=models.DateTimeField(verbose_name='回答日',default=timezone.now)

    def __str__(self):
        return self.text