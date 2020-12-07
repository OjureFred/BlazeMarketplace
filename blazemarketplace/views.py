from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    context = {
        'title': 'Hello Word!!!'
    }

    return render(request, 'home_page.html', context)

def contact_page(request):
    context = {
        'title': 'Contact',
        'content': 'Welcome to contact page'
    }

    if request.method == 'POST':
        print(request.POST)
        print(request.POST.get('fullname'))

    return render(request, 'contacts/view.html', context)