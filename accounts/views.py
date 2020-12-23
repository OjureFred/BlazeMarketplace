from django.shortcuts import render

# Create your views here.
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
    return render(request, 'login.html', context)

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
    return render(request, 'register.html', context)
