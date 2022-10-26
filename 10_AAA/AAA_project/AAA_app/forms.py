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

# class UserForm(forms.ModelForm):
#     first_name = forms.CharField(max_length=50)
#     last_name = forms.CharField(max_length=50)
#     email = forms.EmailField(max_length=100)
#     class Meta:
#         model = User
#         fields = '__all__'