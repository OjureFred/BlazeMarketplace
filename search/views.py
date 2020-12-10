from django.shortcuts import render, get_object_or_404
from django.db.models import Q


from products.models import Product

# Create your views here.
def product_search_view(request):
    search_value =request.GET.q
    queryset = Product.objects.search(search_value)
    context = {'object_list': queryset}

    return render(request, 'search/view.html', context)


