from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm
from django.http import HttpRequest
from django import forms
from django.contrib.auth.models import User
from product.models import Users

class SignUpForm(ModelForm):
    class Meta:
        model = Users
        fields = ['uname','upass','uemail','uadd','uphone']

class LoginForm(AuthenticationForm):
    pass