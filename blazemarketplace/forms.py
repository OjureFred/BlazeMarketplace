from django import forms

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
    password = forms.CharField(widget= forms.PasswordInput(attrs={'class': 'form-control', 'id': 'form-password', 'placeholder': 'Your Name'}))

class RegisterForm(forms.Form):
    username = forms.CharField(widget= forms.TextInput(attrs={'class': 'form-control', 'id': 'form-fullname', 'placeholder': 'Your Name'}))
    email = forms.CharField(widget= forms.EmailInput(attrs={'class': 'form-control', 'id': 'form-fullname', 'placeholder': 'Your Name'}))
    password = forms.CharField(widget= forms.PasswordInput(attrs={'class': 'form-control', 'id': 'form-fullname', 'placeholder': 'Your Name'}))
    password2 = forms.CharField(widget= forms.PasswordInput(attrs={'class': 'form-control', 'id': 'form-fullname', 'placeholder': 'Your Name'}))