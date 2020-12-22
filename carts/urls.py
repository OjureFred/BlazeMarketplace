from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include

from . import views

urlpatterns = [
path('cart/', views.cart_home, name='cart_home'),
path('cart_update/', views.cart_update, name='update_cart'),
path('checkout/', views.checkout_home, name='checkout'),
]

