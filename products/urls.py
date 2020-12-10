from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include

from . import views

urlpatterns = [
path('list/', views.product_list_view, name='products_list'),
path('detail/<pk>/', views.product_detail_view, name='product_detail'),
path('featured/', views.product_featured_list_view, name='featured_list'),
path('product/<slug>/', views.product_slug_view, name='detail')

]

