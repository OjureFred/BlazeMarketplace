from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.models import User

from django.conf.urls.static import static

from .forms import ContactForm, LoginForm, RegisterForm

def home_page(request):
    print(static)
    context = {
        'title': 'Hello Word!!!'
        
    }

    if request.user.is_authenticated:
        context['premium_content'] = 'This is premium content only for logged in users'

    return render(request, 'home_page.html', context)

def login_page(request):
    form = LoginForm(request.POST or None)
    print(request.user.is_authenticated)
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('login_page')
        else:
            print('Error')
            

    context = {
        'title': 'Login Page',
        'form': form
    }
    return render(request, 'auth/login.html', context)

user = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)

    context = {
        'title': 'Register Page',
        'form': form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        new_user = User.objects.create_user(username, email, password)
        print(new_user)
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