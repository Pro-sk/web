from django.shortcuts import render,redirect
from django.contrib import messages
from .form import SignUpForm,LoginForm
from django import forms
from django.http import HttpRequest
def Signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'Succesfully signed up!!!')
        else:
            messages.add_message(request,messages.WARNING,'Something Error!!!')
    else:
        form = SignUpForm()
    return render(request,'log.html',{'form':form})

def login(request):
    if request.method=="POST":
        form = LoginForm(request.POST) 
        if form.is_valid():
            messages.add_message(request,messages.SUCCESS,'Succesfully signed up!!!')
        else:
            messages.add_message(request,messages.WARNING,'Something Error!!!')
    else:
        form = LoginForm()
    return render(request,'log.html',{'form':form})
# Create your views here.
