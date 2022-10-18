from django.shortcuts import render
from static_media_app.models import Topic, Webpage, AccessRecord

# Create your views here.

# A view is a function or method that takes http requests as 
# arguments, imports the relevant model(s), and finds out what 
# data to send to the template, and returns the final result.

def index(request):

    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}

    # The models are imported from the models.py file.
    # The view then sends the data to a specified template in the template folder.
    return render( request, 'static_media_app/static_media_index.html', date_dict)

    # (for the first project)
    # template_tag = {'temp_tag_one':'this is from the views.py file in the app, this is a template tag'}