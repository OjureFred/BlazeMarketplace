from django.shortcuts import render

# Create your views here.
def cart_home(request):
    context = {'title': 'Blazemarket Shopping Cart'}
    print(dir(request.session))
    return render(request, 'carts/home.html', context)
