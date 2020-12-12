from django.shortcuts import render, redirect

from products.models import Product

from .models import Cart
#from products.models import Product

# Create your views here.
def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
            
    context = {'title': 'Blazemarket Shopping Cart', 'cart_obj': cart_obj}
   
    return render(request, 'carts/home.html', context)

def cart_update(request):
    print(request.POST)
    product_id = 1
    product_obj = Product.objects.get(id=product_id)
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    if product_obj in cart_obj.products.all():
        cart_obj.products.remove(product_obj)
    else:
        cart_obj.products.add(product_obj)

    return redirect('cart_home')
