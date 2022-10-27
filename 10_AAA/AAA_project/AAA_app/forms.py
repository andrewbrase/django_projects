from django import forms
from .models import Account

class AccountForm(forms.ModelForm):
    firstname = forms.CharField(label='First Name:', widget=forms.TextInput(attrs={'placeholder': 'First Name', 'required': 'true'}))
    lastname = forms.CharField(label='Last Name:', widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'required': 'true'}))
    email = forms.CharField(label='Email:', widget=forms.TextInput(attrs={'placeholder': 'example@domain.com', 'required': 'true'}))
    password = forms.CharField(label='Password:', widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'required': 'true'}))
    class Meta:
        model = Account
        fields = '__all__'

    def clean(self):
        # if you use super you will grab all of the data at once
        # all_clean_data = super().clean()

        if Account.objects.filter(email=self.cleaned_data['email']).exists():
            # change this
            raise forms.ValidationError("The given email is already registered")