from django.shortcuts import render
from .forms import AccountForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def signup(request):

    form = AccountForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return index(request)

    return render(request, 'signup.html', {'form':form})