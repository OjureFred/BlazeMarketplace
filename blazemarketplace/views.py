from django.http import HttpResponse
from django.shortcuts import render

from .forms import ContactForm

def home_page(request):
    context = {
        'title': 'Hello Word!!!'
    }

    return render(request, 'home_page.html', context)

def contact_page(request):
    contact_form = ContactForm()
    context = {
        'title': 'Contact',
        'content': 'Welcome to contact page',
        'form': contact_form
    }

    if request.method == 'POST':
        print(request.POST)
        print(request.POST.get('fullname'))

    return render(request, 'contacts/view.html', context)