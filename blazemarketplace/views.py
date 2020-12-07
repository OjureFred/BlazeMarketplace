from django.http import HttpResponse
from django.shortcuts import render

from .forms import ContactForm, LoginForm, RegisterForm

def home_page(request):
    context = {
        'title': 'Hello Word!!!'
    }

    return render(request, 'home_page.html', context)

def login_page(request):
    form = LoginForm(request.POST or None)
    #print(request.user.is_authenticated())
    if form.is_valid():
        print(form.cleaned_data)

    context = {
        'title': 'Login Page',
        'form': form
    }
    return render(request, 'auth/login.html', context)

def register_page(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)

    context = {
        'title': 'Register Page',
        'form': form
    }
    return render(request, 'auth/register.html', context)

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