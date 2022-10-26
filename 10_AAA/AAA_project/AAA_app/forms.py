from django import forms
from .models import Account

class AccountForm(forms.ModelForm):
    # firstname = forms.CharField(max_length=50)
    # lastname = forms.CharField(max_length=50)
    # email = forms.EmailField(max_length=70)
    # password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = '__all__'