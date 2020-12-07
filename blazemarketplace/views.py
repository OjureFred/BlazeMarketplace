from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    context = {
        'title': 'Hello Word!!!'
    }
    return render(request, 'home_page.html', context)