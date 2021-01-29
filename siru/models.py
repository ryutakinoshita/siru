from django.db import models
from accounts.models import User



class Contact(models.Model):
    name=models.ForeignKey(User,verbose_name='ユーザー',on_delete=models.CASCADE)
    email=models.EmailField(max_length=200,verbose_name='Eメール',blank=False,null=False)
    message=models.TextField(max_length=2000,verbose_name='内容',blank=False,null=False)

    def __str__(self):
        return self.message
