from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Laptop,feedback
import datetime

# Create your views here.
def home(request):
    filterPara = ''
    if request.POST.get('sort'):
        if request.POST.get('filterPara')!='':
            filterPara = request.POST.get('filterPara')
            fprice = filterPara.split(',')[0]
            lprice = filterPara.split(',')[1]
            if request.POST.get('sort') == 'P+':
                laptops = Laptop.objects.filter(price__range = (fprice,lprice)).order_by('price')
            elif request.POST.get('sort') == 'P-':
                laptops = Laptop.objects.filter(price__range = (fprice,lprice)).order_by('-price')
            elif request.POST.get('sort') == 'N+':
                laptops = Laptop.objects.filter(price__range = (fprice,lprice)).order_by('pname')
            elif request.POST.get('sort') == 'N-':
                laptops = Laptop.objects.filter(price__range = (fprice,lprice)).order_by('-pname')
        else:
            if request.POST.get('sort') == 'P+':
                laptops = Laptop.objects.all().order_by('price')
            elif request.POST.get('sort') == 'P-':
                laptops = Laptop.objects.all().order_by('-price')
            elif request.POST.get('sort') == 'N+':
                laptops = Laptop.objects.all().order_by('pname')
            elif request.POST.get('sort') == 'N-':
                laptops = Laptop.objects.all().order_by('-pname')
    elif request.POST.get('filter'):
        filterPara = request.POST.get('filter')
        fprice = filterPara.split(',')[0]
        lprice = filterPara.split(',')[1]
        laptops = Laptop.objects.filter(price__range = (fprice,lprice))
    else:
        laptops = Laptop.objects.all()
    return render(request,"laptops.html",{'laptop':laptops,'filterPara':filterPara})

def viewLaptop(request,id):
    if request.method == "POST":
        pid = request.POST['pid']
        star = request.POST['star']
        msg = request.POST['msg'].strip()
        uname = request.user.username
        form = feedback(uname=uname,msg=msg,star=star,pid=pid,udate=datetime.datetime.now())
        form.save()
        messages.success(request,'Successfully written your feedback !!!')
    else:
        pass
    feed = feedback.objects.filter(pid=id).order_by('-pk')[:4]
    laptop = Laptop.objects.filter(id=id)
    pdesc = laptop[0].pdesc
    related = Laptop.objects.filter(pdesc=pdesc)
    return render(request,"laptop.html",{'laptop':laptop,'related':related,'feed':feed})