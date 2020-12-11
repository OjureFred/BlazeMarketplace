from django.shortcuts import render

from .models import Cart
#from products.models import Product

# Create your views here.
def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
            
    context = {'title': 'Blazemarket Shopping Cart', 'cart_obj': cart_obj}
   
    return render(request, 'carts/home.html', context)
