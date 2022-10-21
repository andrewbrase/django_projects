from django.shortcuts import render
from . import forms
# Create your views here.

def index(request):
    return render(request, 'index.html')

def form_name_view(request):
    form = forms.FormName()
    return render(request, 'form_page.html', {'form_t' : form})

    # we need to save the POST data 13:54