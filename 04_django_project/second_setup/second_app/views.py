from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

def index(request):
    my_second_dict = {'first_template_tag':'this is from the views.py file in the second app'}
    return render(request, 'second_app/index.html', context= my_second_dict)
    # my_dict = {'insert_me':'this is from the views.py file in the app, this is the template tag'}
    # return render( request, 'first_app/index.html', context= my_dict )