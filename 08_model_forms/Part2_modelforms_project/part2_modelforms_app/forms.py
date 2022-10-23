from django import forms
from part2_modelforms_app.models import User
from django.core import validators

class UserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=100)
    class Meta:
        model = User
        fields = '__all__'