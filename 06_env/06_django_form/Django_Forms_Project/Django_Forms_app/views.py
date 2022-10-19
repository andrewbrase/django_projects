from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Members

# Create your views here.

def index(request):
    # return HttpResponse("Hello world!")
    # return HttpResponse(template.render())

    mymembers = Members.objects.all().values()
    template = loader.get_template('df.html')
    context = {
        'mymembers_t' : mymembers,
    }
    return HttpResponse(template.render(context, request))
    # output = ""
    # for member in mymembers:
    #     output += member["firstname"]
    # return HttpResponse(output)