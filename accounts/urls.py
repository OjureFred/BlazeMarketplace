from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from . import views

urlpatterns = [
path('login_page', views.login_page, name = 'login_page'),
path('register_page', views.register_page, name='register_page'),
path('register/guest/', views.guest_register_view, name='guest_register_view'),
]

