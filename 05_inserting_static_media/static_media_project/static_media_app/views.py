from django.shortcuts import render
from static_media_app.models import Topic, Webpage, AccessRecord

# Create your views here.
def index(request):

    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}

    # template_tag = {'temp_tag_one':'this is from the views.py file in the app, this is a template tag'}
    return render( request, 'static_media_app/static_media_index.html', date_dict)