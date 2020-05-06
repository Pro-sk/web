from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from . import views as v
urlpatterns = [
    path('', v.Signup,name='lasdad'),
    path('login/',v.login,name='logg')
]

    #path('view/phone/<int:id>', views.phone,name='View'),
    #path('view/laptop/<int:id>', views.laptop,name='View'),
    #path('view/tvs/<int:id>', views.tvs,name='View'),
    #
    #
    #
    #path('phone/', views.allphones,name='Cart'),
    #path('laptop/', views.alllaptops,name='phone'),
    #path('tvs/', views.alltvs,name='laptop'),
    #
    #