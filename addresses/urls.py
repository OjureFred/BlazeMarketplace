from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from . import views

urlpatterns = [
path('checkout_address', views.checkout_address_create_view, name = 'login_page'),

]