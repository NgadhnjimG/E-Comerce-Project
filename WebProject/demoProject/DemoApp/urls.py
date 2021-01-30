from django.urls import path
from . import views
from .views import  List_All
from django.conf.urls.static import  static
from django.conf.urls import  url, include
from django.conf import  settings
from django.contrib import admin

urlpatterns = [


    path('',List_All),
    path('cart/', views.cart, name="cart"),

]



if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
