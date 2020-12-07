from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


user = get_user_model()
class ContactForm(forms.Form):
    fullname = forms.CharField(widget= forms.TextInput(attrs={'class': 'form-control', 'id': 'form-fullname', 'placeholder': 'Your Name'}))
    email = forms.CharField(widget= forms.EmailInput(attrs={'class': 'form-control', 'id': 'form-fullname', 'placeholder': 'Your Email'}))
    contact = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'form-content', 'placeholder': 'Your Content '}))
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not 'gmail.com' in email:
            raise forms.ValidationError('Email has to be a gmail account')
        return email

class LoginForm(forms.Form):
    username = forms.CharField(widget= forms.TextInput(attrs={'class': 'form-control', 'id': 'form-username', 'placeholder': 'Your Name'}))
    password = forms.CharField(widget= forms.PasswordInput(attrs={'class': 'form-control', 'id': 'form-password', 'placeholder': 'Password'}))

class RegisterForm(forms.Form):
    username = forms.CharField(widget= forms.TextInput(attrs={'class': 'form-control', 'id': 'form-fullname', 'placeholder': 'Your Name'}))
    email = forms.EmailField(widget= forms.EmailInput(attrs={'class': 'form-control', 'id': 'form-fullname', 'placeholder': 'Your Email'}))
    password = forms.CharField(widget= forms.PasswordInput(attrs={'class': 'form-control', 'id': 'form-fullname', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'form-fullname', 'placeholder': 'Confirm password'}))
    
    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password2 != password:
            raise forms.ValidationError('Passwords must match')
        return data
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError('This username is taken')
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError('This email is taken')
        return email
