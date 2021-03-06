"""blazemarketplace URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))   
"""
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.conf.urls import url,include
from django.urls import path
from .views import home_page, contact_page, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('accounts/', include('accounts.urls')),
    path('address/', include('addresses.urls')),
    path('products/', include('products.urls')),
    path('search/', include('search.urls')),
    path('cart/', include('carts.urls')),
    path('', home_page, name = "home_page"),
    path('contact_page', contact_page, name='contact_page'),
]

if settings.DEBUG:
    urlpatterns += urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    
    urlpatterns += urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
