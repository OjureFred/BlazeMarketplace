from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView

from django.conf.urls.static import static

from .forms import ContactForm, LoginForm, RegisterForm

def home_page(request):
    print(static)
    context = {
        'title': 'Welcome To Alpha Digital Market!!!'
        
    }

    if request.user.is_authenticated:
        context['premium_content'] = 'This is premium content only for logged in users'

    return render(request, 'home_page.html', context)



def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    context = {
        'title': 'Contact',
        'content': 'Welcome to contact page',
        'form': contact_form
        
    }

    if request.method == 'POST':
        print(request.POST)
        print(request.POST.get('fullname'))

    return render(request, 'contacts/view.html', context)