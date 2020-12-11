from django.shortcuts import render

from .models import Cart
from products.models import Product

# Create your views here.
def cart_create(user=None):
    product = Product.objects.get(id=1)
    cart_obj = Cart.objects.create(user=None, products=product)

def cart_home(request):
    request.session['cart_id'] = 12
    cart_id = request.session.get('cart_id', None)
    qs = Cart.objects.filter(id = cart_id)
    if qs.count() == 1:
        print('Cart ID exists')
        cart_obj = qs.first()
    else:
        cart_obj = cart_create()
        #request.session['cart_id']= cart_obj.id
        
    context = {'title': 'Blazemarket Shopping Cart', 'cart_id': cart_id}
   
    return render(request, 'carts/home.html', context)
