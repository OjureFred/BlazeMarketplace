from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from products.views import product_list_view

from.views import product_search_view

urlpatterns = [
path('', product_search_view, name='products_list'),

]