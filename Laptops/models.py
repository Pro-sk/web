from django.db import models

# Create your models here.
class Laptop(models.Model):
    pname = models.CharField(max_length=50,default="")
    pdesc = models.CharField(max_length=200)
    pcategory = models.CharField(max_length=50)
    memory = models.CharField(max_length=200)
    harddisk = models.CharField(max_length=200)
    processor = models.CharField(max_length=200)
    price = models.IntegerField()
    pimg = models.ImageField()

    def __str__(self):
        return self.pname


class feedback(models.Model):
    uname = models.CharField(max_length=50)
    msg = models.CharField(max_length=300)
    star = models.IntegerField(max_length=5)
    pid = models.IntegerField(max_length=20)
    udate = models.DateField(auto_now=True)

    def __str__(self):
        return self.uname


