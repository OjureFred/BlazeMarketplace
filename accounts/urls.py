from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from . import views

urlpatterns = [
path('login_page', login_page, name = 'login_page'),
path('register_page', register_page, name='register_page'),
]

