from django.shortcuts import render
from part2_modelforms_app.forms import UserForm
# from part2_modelforms_app.models import User
# from . import forms

# Create your views here.

def index(request):
    return render(request, 'index.html')

def users(request):
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Error, form is invalid')

    return render(request, 'users.html', context= {'form_t' : form})

    # form = forms.UserForm()

    # user_list = User.objects.order_by('first_name')
    # user_dict = {'users_t': user_list, 'form_t' : form}

    # if request.method == 'POST':
    #     form = forms.UserForm(request.POST)

    #     # is_valid is a boolean check
    #     if form.is_valid():
    #         # do something code
    #         print('form validation successful')

    # return render(request, 'users.html', context= user_dict)


# def addrecord(request):
#     first = request.POST['first_name']
#     last = request.POST['last_name']
#     new_email = request.POST['email']
#     new_user = User(first_name=first, last_name=last, email=new_email)
#     new_user.save()
#     return render(request, 'index.html')

