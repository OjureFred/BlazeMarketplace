from django.shortcuts import render

from .models import Cart
from products.models import Product

# Create your views here.
def cart_create(user=None):
    product = Product.objects.get(id=1)
    cart_obj = Cart.objects.create(user=None, products=product)

def cart_home(request):
    cart_id = request.session.get('cart_id', None)
    if cart_id is None:
        cart_obj = cart_create()
        request.session['cart_id'] = cart_obj.id
    else:
        qs = Cart.objects.filter(id=cart_id)
        if qs.count() == 1:
            print('Cart ID exists')
            print(cart_id)
            cart_obj = qs.first()
        else:
            cart_obj = cart_create()
            request.session['cart_id']= cart_obj.id
        
    context = {'title': 'Blazemarket Shopping Cart'}
   
    return render(request, 'carts/home.html', context)
