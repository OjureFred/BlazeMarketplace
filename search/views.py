from django.shortcuts import render, get_object_or_404


from products.models import Product

# Create your views here.
def product_search_view(request):
    queryset = Product.objects.filter(title__icontains='hat')
    print(request.GET)
    context = {'object_list': queryset}

    return render(request, 'search/view.html', context)
