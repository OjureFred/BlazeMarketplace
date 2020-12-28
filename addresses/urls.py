from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from . import views

urlpatterns = [
path('checkout_address_create', views.checkout_address_create_view, name = 'checkout_address_create'),

]