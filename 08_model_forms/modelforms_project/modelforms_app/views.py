from django.shortcuts import render
from . import forms
# Create your views here.

def index(request):
    return render(request, 'index.html')

def form_name_view(request):
    form = forms.FormName()
    # [22/Oct/2022 20:09:29] "POST /formpage/ HTTP/1.1" 200 1348
    # after the form data has been posted

    # this means if someone has hit submit and posted something back
    if request.method == 'POST':
        form = forms.FormName(request.POST)

        # is_valid is a boolean check
        if form.is_valid():
            # do something code
            print('form validation successful')
            # how to access that data, in the form 
            # you have the class obj attributes name, email and text, 
            # thats what you pass in as the key
            print('NAME: ' + form.cleaned_data['name'])
            print('EMAIL: ' + form.cleaned_data['email'])
            print('TEXT: ' + form.cleaned_data['text'])
            # [22/Oct/2022 20:21:44] "GET /formpage/ HTTP/1.1" 200 1348
            # form validation successful
            # Andrew
            # andrewbrase1@yahoo.com
            # test
            # [22/Oct/2022 20:21:49] "POST /formpage/ HTTP/1.1" 200 1398

    return render(request, 'form_page.html', {'form_t' : form})
