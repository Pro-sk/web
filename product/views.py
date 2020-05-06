from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from PHones.models import Phone
from Laptops.models import Laptop
from Tvss.models import Tvs
from .models import Cart
from .models import Users,Order
from .form import Signup,Login
from .import checksum
from random import randint
import json
import datetime
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    #return HttpResponse(Product.pname)
    phone = Phone.objects.all()[:6]
    laptop = Laptop.objects.all()[:6]
    tvs = Tvs.objects.all()[:6]
    return render(request,"index.html",{'phone':phone,'laptop':laptop,'tvs':tvs})

def addToCart(request,id,category,frm='view'):
    if request.session.get('phone'):
        phone = request.session['phone']
        checkIfAlreadyAdded = Cart.objects.filter(pid=id,uphone=phone,pcategory=category.lower())
        if len(checkIfAlreadyAdded)<=0:
            if category=="Phone":
                product = Phone.objects.filter(id=id)
            elif category=="Laptop":
                product = Laptop.objects.filter(id=id)
            else:
                product = Tvs.objects.filter(id=id)
            addData = Cart.objects.create(pid=id,uphone=phone,pname=product[0].pname,pdesc=product[0].pdesc,pcategory=product[0].pcategory,price=product[0].price,pimg=product[0].pimg)
            addData.save()
            messages.add_message(request,messages.SUCCESS,"Successfully Added!!!")
            if frm=='view':
                return redirect('/'+category.lower()+'/view/'+str(id))
            else:
                pass
        else:
            if frm=='view':
                messages.add_message(request,messages.WARNING,"Product is Already Added!!!")
            else:
                pass
            return redirect('/'+category.lower()+'/view/'+str(id))
    else:
        return redirect('/login/')

def cart(request):
    if request.method=="POST":
        id = request.POST.get('id')
        category = request.POST.get('category')
        Cart.objects.filter(pid=id,pcategory=category).delete()
        messages.add_message(request,messages.SUCCESS,"Successfully removed")
    else:
        pass
    cartData = Cart.objects.filter(uphone=request.session.get('phone'))
    return render(request,'cart.html',{'cart':cartData})

def buy(request,category):
    if request.session.get('phone'):
        if request.method == 'POST':
            id = request.POST.get('id')
            addToCart(request,id,category,frm='buy')
            cart = Cart.objects.all()
            cartData = Cart.objects.filter(uphone=request.session.get('phone'))
            return redirect('/cart/')
        else:
            pass
    else:
        return redirect('/login/')

def buyPage(request):
    cartData = Cart.objects.filter(uphone=request.session.get('phone'))
    price = []
    for i in cartData:
        price.append(i.price)
    user = Users.objects.filter(uphone=request.session.get('phone'))
    return render(request,'buy.html',{'cart':cartData,'user':user,'total':sum(price)})


def payment(request):
    cartData = Cart.objects.filter(uphone=request.session.get('phone'))
    price = []
    for i in cartData:
        price.append(i.price)

    #user = Users.objects.filter(uphone=request.session.get('phone'))
    # initialize dictionary with request parameters
    paytmParams = {

	# Find your MID in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys
	"MID" : "EBVhRV83907159364389",

	# Find your WEBSITE in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys
	"WEBSITE" : "WEBSTAGING",

	# Find your INDUSTRY_TYPE_ID in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys
	"INDUSTRY_TYPE_ID" : "Retail",

	# WEB for website and WAP for Mobile-websites or App
	"CHANNEL_ID" : "WEB",

	# Enter your unique order id
	"ORDER_ID" : str(randint(1000,9999)),

	# unique id that belongs to your customer
	"CUST_ID" : str(request.user.id),

	# customer's mobile number
	"MOBILE_NO" : request.session.get('phone'),

	# customer's email
	"EMAIL" : str(request.user.email),

	# Amount in INR that is payble by customer
	# this should be numeric with optionally having two decimal points
	"TXN_AMOUNT" : str(sum(price)),

	# on completion of transaction, we will send you the response on this URL
	"CALLBACK_URL" : "http://127.0.0.1:8000/thanks/",
    }
    cartD = Cart.objects.filter(uphone=request.session.get('phone'))
    for item in cartD:
        order = Order(uphone=item.uphone,pname=item.pname,pdesc=item.pdesc,pcategory=item.pcategory,price=item.price,pimg=item.pimg,orderdate=datetime.datetime.now(),orderid=paytmParams['ORDER_ID'])
        order.save()
    #for item in cartD:
        #Order.objects.create(uphone=item.uphone,pname=item.pname,pdesc=item.pdesc,pcategory=item.pcategory,price=item.price,pimg=item.pimg,orderdate=datetime.datetime.now())
    paytmParams['CHECKSUMHASH'] = checksum.generate_checksum(paytmParams, "K5hQyqA7CU1RUj!%")
    return render(request,"paytm.html",{'data':paytmParams})


@csrf_exempt
def thanks(request):
    data = request.POST
    jsdata = json.dumps(data)
    order = Order.objects.filter(uphone=request.session.get('phone')).order_by('-id')
    #i = 0
    for item in range(0,len(order)):
        #i = i+1
        order = Order.objects.get(uphone=request.session.get('phone')).order_by('-pk')
        order.jsondata = jsdata
        order.save()
    Cart.objects.all().filter(uphone=request.session.get('phone')).delete()
    return HttpResponse(jsdata)
    #return render(request,"thanks.html",{'data':data})


def Search(request):
    filterPara = ''
    pattern = request.POST.get('pattern')
    if request.POST.get('search'):
        pattern = request.POST.get('search')
        phones = Phone.objects.filter(pname__icontains=pattern)
        laptop = Laptop.objects.filter(pname__icontains=pattern)
        tvs = Tvs.objects.filter(pname__icontains=pattern)
    if request.POST.get('sort'):
        pattern = request.POST.get('pattern')
        if request.POST.get('filterPara')!='':
            filterPara = request.POST.get('filterPara')
            fprice = filterPara.split(',')[0]
            lprice = filterPara.split(',')[1]
            if request.POST.get('sort') == 'P+':
                phones = Phone.objects.filter(pname__icontains=pattern,price__range = (fprice,lprice)).order_by('price')
                laptop = Laptop.objects.filter(pname__icontains=pattern,price__range = (fprice,lprice)).order_by('price')
                tvs = Tvs.objects.filter(pname__icontains=pattern,price__range = (fprice,lprice)).order_by('price')
            elif request.POST.get('sort') == 'P-':
                phones = Phone.objects.filter(pname__icontains=pattern,price__range = (fprice,lprice)).order_by('-price')
                laptop = Laptop.objects.filter(pname__icontains=pattern,price__range = (fprice,lprice)).order_by('-price')
                tvs = Tvs.objects.filter(pname__icontains=pattern,price__range = (fprice,lprice)).order_by('-price')
            elif request.POST.get('sort') == 'N+':
                phones = Phone.objects.filter(pname__icontains=pattern,price__range = (fprice,lprice)).order_by('pname')
                laptop = Laptop.objects.filter(pname__icontains=pattern,price__range = (fprice,lprice)).order_by('pname')
                tvs = Tvs.objects.filter(pname__icontains=pattern,price__range = (fprice,lprice)).order_by('pname')
            elif request.POST.get('sort') == 'N-':
                phones = Phone.objects.filter(pname__icontains=pattern,price__range = (fprice,lprice)).order_by('-pname')
                laptop = Laptop.objects.filter(pname__icontains=pattern,price__range = (fprice,lprice)).order_by('-pname')
                tvs = Tvs.objects.filter(pname__icontains=pattern,price__range = (fprice,lprice)).order_by('-pname')
        else:
            pattern = request.POST.get('pattern')
            if request.POST.get('sort') == 'P+':
                phones = Phone.objects.filter(pname__icontains=pattern).order_by('price')
                laptop = Laptop.objects.filter(pname__icontains=pattern).order_by('price')
                tvs = Tvs.objects.filter(pname__icontains=pattern).order_by('price')
            elif request.POST.get('sort') == 'P-':
                phones = Phone.objects.filter(pname__icontains=pattern).order_by('-price')
                laptop = Laptop.objects.filter(pname__icontains=pattern).order_by('-price')
                tvs = Tvs.objects.filter(pname__icontains=pattern).order_by('-price')
            elif request.POST.get('sort') == 'N+':
                phones = Phone.objects.filter(pname__icontains=pattern).order_by('pname')
                laptop = Laptop.objects.filter(pname__icontains=pattern).order_by('pname')
                tvs = Tvs.objects.filter(pname__icontains=pattern).order_by('pname')
            elif request.POST.get('sort') == 'N-':
                phones = Phone.objects.filter(pname__icontains=pattern).order_by('-pname')
                laptop = Laptop.objects.filter(pname__icontains=pattern).order_by('-pname')
                tvs = Tvs.objects.filter(pname__icontains=pattern).order_by('-pname')
    elif request.POST.get('filter'):
        filterPara = request.POST.get('filter')
        fprice = filterPara.split(',')[0]
        lprice = filterPara.split(',')[1]
        phones = Phone.objects.filter(pname__icontains=pattern,price__range = (fprice,lprice))
        laptop = Laptop.objects.filter(pname__icontains=pattern,price__range = (fprice,lprice))
        tvs = Tvs.objects.filter(pname__icontains=pattern,price__range = (fprice,lprice))
    return render(request,"search.html",{'phone':phones,'laptop':laptop,'tvs':tvs,'pattern':pattern,'filterPara':filterPara})

def logout(request):
    del request.session['phone']
    return redirect('/')

def log(request):
    if request.method == "POST":
        form = Login(request.POST)
        uphone = request.POST.get('uphone')
        upass = request.POST.get('upass')
        #user = authenticate(request,uphone=uphone,upass=upass)
        result = Users.objects.filter(uphone=uphone,upass=upass)
        if len(result)==1:
            request.session['phone'] = uphone
            return redirect('/')
        else:
            messages.set_level(request, messages.WARNING)
            #messages.add_message(request, messages.INFO ,'Invalid Phone Number and Password')
            messages.warning(request,'Invalid Phone Number and Password',fail_silently=True)
            return redirect('/login/')
    else:
        form = Login()
        return render(request,'login.html',{'form':form})

def signup(request):
    if request.method == "POST":
        form = Signup(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Successfully signup")
            return redirect('/login/')
        else:
            return render(request,'signup.html',{'form':form})
            
    else:
        form = Signup()
        return render(request,'signup.html',{'form':form})
