from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Product

# Create your views here.
def product_list_view(request):
    queryset = Product.objects.all()
    context = {'object_list': queryset}

    return render(request, 'product/list.html', context)

def product_detail_view(request, pk):
    instance = Product.objects.get_by_id(pk)
    if instance is None:
        raise Http404("Product does not exist")
    print(instance)
    context = {'object': instance}

    return render(request, 'product/detail.html', context)

def product_featured_list_view(request):
    queryset = Product.objects.filter(featured=True)
    context = {'object_list': queryset}

    return render(request, 'product/list.html', context)

def product_slug_view(request, slug):
    instance = Product.objects.get(slug=slug)
    context = {'object': instance}

    return render(request, 'product/detail.html', context)

def get_absolute_url(self):
    return reverse('detail', kwargs={'slug': self.slug})