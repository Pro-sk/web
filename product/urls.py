from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('', views.index,name='Home'),
    path('addtocart/<int:id>/<str:category>', views.addToCart,name='AddToCart'),
    path('cart/', views.cart,name='tvs'),
    path('buy/<str:category>/',views.buy,name='buy'),
    path('buy/',views.buyPage,name='buy'),
    path('search/', views.Search,name='Search'),
    path('login/', views.log,name='Login'),
    path('logout/', views.logout,name='Logout'),
    path('signup/', views.signup,name='Signup'),
    path('payment/', views.payment,name='payment'),
    path('thanks/', views.thanks,name='thanks'),
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