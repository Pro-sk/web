from django.contrib import admin
from .models import Users,Order,Cart
admin.site.register(Cart)
admin.site.register(Users)
admin.site.register(Order)