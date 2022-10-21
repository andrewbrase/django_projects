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
    item_name_list = foodItem.objects.order_by('item_name')
    item_dict = {'cart_t':item_name_list}
    cart_template = loader.get_template('cart.html')
    # return HttpResponse(cart_template.render())
    return render(request, 'cart.html', context=item_dict)

    # user_list = User.objects.order_by('firstname')
    # user_dict = {'users_t': user_list}
    # return render(request, 'users.html', context=user_dict)


def store(request):
    store_template = loader.get_template('store.html')
    return HttpResponse(store_template.render())