from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser
# Create your models here. 
class Users(AbstractBaseUser):
    uname = models.CharField(verbose_name="Username",max_length=50,default="")
    uemail = models.EmailField(verbose_name="Email")
    uadd = models.CharField(verbose_name="Address",max_length=150,default="")
    upass = models.CharField(verbose_name="Password",max_length=150,default="")
    city = models.CharField(verbose_name="City",max_length=100,default="")
    zip = models.IntegerField(verbose_name="ZipCode",max_length=6)
    state = models.CharField(verbose_name="State",max_length=200,default="")
    uphone = models.CharField(verbose_name="Phone",primary_key=True,max_length=10,default="",unique=True)

    USERNAME_FIELD = 'uphone'
    REQUIRED_FIELDS = ['uname','uemail','upass','uadd','city','zip','state']

    def __str__(self):
        return self.uname


class Cart(models.Model):
    pid = models.IntegerField(primary_key=False)
    uphone = models.CharField(max_length=50,default='')
    pname = models.CharField(max_length=50,default="")
    pdesc = models.CharField(max_length=200)
    pcategory = models.CharField(max_length=50)
    price = models.IntegerField()
    pimg = models.ImageField()

    def __str__(self):
        return self.pname

class Order(models.Model):
    uphone = models.CharField(max_length=50,default='')
    pname = models.CharField(max_length=50,default="")
    pdesc = models.CharField(max_length=200)
    pcategory = models.CharField(max_length=50)
    price = models.IntegerField()
    pimg = models.ImageField()
    orderid = models.CharField(max_length=20,default="")
    orderdate = models.DateField(auto_now_add=False)
    jsondata = models.CharField(max_length=1000,default="")

    def __str__(self):
        return self.uphone