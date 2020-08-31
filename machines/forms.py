from django import forms
from .models import Company, AdminList



class RegForm(forms.ModelForm):
    name = forms.CharField(max_length=100, label="Név: ")
    email = forms.EmailField(max_length=254, label="Email cím: ")
    user = forms.CharField(max_length=10, label="Választott felhasználónév: ")
    password = forms.CharField(widget=forms.PasswordInput, label="Jelszó: " )
    

    class Meta:
        model = Company
        fields = ('name', 'email', 'user', 'password')

class HomeForm(forms.Form):
    user = forms.CharField(max_length=30, label="Felhasználónév ")
    password = forms.CharField(widget=forms.PasswordInput, label="Jelszó ")

    
    

    