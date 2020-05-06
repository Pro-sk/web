from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('',views.home,name='Home'),
    path('view/<int:id>',views.viewPhone,name='viewPhone'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
