from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from accounts.models import  User


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = [

            "username", "profile",'email','password1', 'password2',
        ]


class UserChangeForm(ModelForm):
    class Meta:
        model=User
        fields=[
            "username","profile",
        ]

    def __init__(self,username=None,profile=None,*args,**kwargs):
        kwargs.setdefault('label_suffix','')
        super().__init__(*args,**kwargs)
        if username:
            self.fields['username'].widget.attrs['value'] = username
        if profile:
            self.fields['profile'].widget.attrs['value'] = profile


    def update(self, user):
        user.username = self.cleaned_data['username']
        user.profile = self.cleaned_data['profile']
        user.save()