from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# This is a simple example on how to send a response back to the browser
def index(request):
    return HttpResponse("Hello World")
# But how can we execute the view? Well, we must call the view via a URL.