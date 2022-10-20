# from json import load
# from re import template
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
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

def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))

def addrecord(request):
    x = request.POST['first']
    y = request.POST['last']
    member = Members(firstname=x, lastname=y)
    member.save()
    return HttpResponseRedirect(reverse('index'))

# The delete view does the following:
# Gets the id as an argument.
# Uses the id to locate the correct record in the Members table.
# Deletes that record.
# Redirects the user back to the index view.
def delete(request, id):
    member = Members.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('index'))

# The update view does the following:
# Gets the id as an argument.
# Uses the id to locate the correct record in the Members table.
# loads a template called update.html.
# Creates an object containing the member.
# Sends the object to the template.
# Outputs the HTML that is rendered by the template.

def update(request, id):
    mymember = Members.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
        'mymember_t':mymember,
    }
    return HttpResponse(template.render(context, request))

def updaterecord(request, id):
    first = request.POST['first']
    last = request.POST['last']
    member = Members.objects.get(id=id)
    member.firstname = first
    member.lastname = last
    member.save()
    return HttpResponseRedirect(reverse('index'))