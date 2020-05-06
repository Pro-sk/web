from django.shortcuts import render,redirect
# Create your views here.
from django.http import HttpResponse
from product.models import Users
from product.form import Signup
from django.contrib import messages

def index(request):
    return render(request,"index.html")

def userAccount(request,frm=""):
    phone = request.session.get('phone')
    form = Users.objects.filter(uphone=phone)
    return render(request,'account.html',{'form':form})

def updateAccount(request):
    phone = request.session.get('phone')
    userData = Users.objects.filter(uphone=phone)
    if request.method=="POST":
        uname = request.POST.get('uname')
        email = request.POST.get('email')
        uphone = request.POST.get('phone')
        password = request.POST.get('password')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zipD = request.POST.get('zip')
        Users.objects.filter(uphone=phone).update(uname=uname,uemail=email,uadd=address,city=city,state=state,zip=zipD)
        messages.add_message(request,messages.SUCCESS,'Successfully Updated')
        return redirect('/account/')
    else:
        return render(request,'update.html',{'form':userData})