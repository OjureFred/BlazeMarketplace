from django import forms

class ContactForm(forms.Form):
    fullname = forms.CharField(widget= forms.TextInput(attrs={'class': 'form-control', 'id': 'form-fullname', 'placeholder': 'Your Name'}))
    email = forms.CharField(widget= forms.TextInput(attrs={'class': 'form-control', 'id': 'form-fullname', 'placeholder': 'Your Email'}))
    contact = forms.CharField(widget= forms.Textarea(attrs={'class': 'form-control', 'id': 'form-content', 'placeholder': 'Your Content '}))