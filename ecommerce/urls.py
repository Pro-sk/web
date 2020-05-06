from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('log/',include('user.urls'),name='Log'),
    path('',include('product.urls'),name=''),
    path('phone/',include('PHones.urls'),name='Phone'),
    path('laptop/',include('Laptops.urls'),name='Laptop'),
    path('tvs/',include('Tvss.urls'),name='Tvs'),
    path('account/',views.userAccount,name='account'),
    path('account/update/',views.updateAccount,name='update_account'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
