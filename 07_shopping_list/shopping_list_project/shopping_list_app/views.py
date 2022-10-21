from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import foodItem, tv

# Create your views here.

def index(request):
    # return HttpResponse("Hello World!")
    index_template = loader.get_template('index.html')
    return HttpResponse(index_template.render())

def cart(request):
    cart_template = loader.get_template('cart.html')
    return HttpResponse(cart_template.render())

def store(request):
    store_template = loader.get_template('store.html')
    return HttpResponse(store_template.render())