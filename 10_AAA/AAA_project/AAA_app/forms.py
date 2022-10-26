from django import forms
from .models import Account

class AccountForm(forms.ModelForm):
    firstname = forms.CharField(label='First Name:', widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    lastname = forms.CharField(label='Last Name:', widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    email = forms.CharField(label='Email:', widget=forms.TextInput(attrs={'placeholder': 'example@domain.com'}))
    password = forms.CharField(label='Password:', widget=forms.PasswordInput)
    class Meta:
        model = Account
        fields = '__all__'