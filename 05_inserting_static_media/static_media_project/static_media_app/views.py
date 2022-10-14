from django.shortcuts import render

# Create your views here.
def index(request):
    template_tag = {'temp_tag_one':'this is from the views.py file in the app, this is a template tag'}
    return render( request, 'static_media_app/static_media_index.html', template_tag)