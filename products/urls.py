from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include

from . import views

urlpatterns = [
path('list/', views.product_list_view, name='products_list'),
path('detail/<pk>/',  views.product_detail_view, name='product_detail'),

]

