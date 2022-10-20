from django.shortcuts import render
from Practice_App.models import User
# Create your views here.

def index(request):
    return render(request, 'index.html')

def users(request):
    user_list = User.objects.order_by('firstname')
    user_dict = {'users_t': user_list}
    return render(request, 'users.html', context=user_dict)

# py manage.py migrate
# py manage.py makemigrations Practice_App
# py manage.py migrate
