from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Members

# Create your views here.

def index(request):
    # return HttpResponse("Hello world!")

    # template = loader.get_template('df.html')
    # return HttpResponse(template.render())

    mymembers = Members.objects.all().values()
    output = ""
    for member in mymembers:
        output += member["firstname"]
    return HttpResponse(output)