from django.contrib import admin

# Register your models here.
from .models import Tvs,feedback
admin.site.register(Tvs)
admin.site.register(feedback)