from django import forms

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    # https://docs.djangoproject.com/en/4.1/ref/forms/widgets/#built-in-widgets
