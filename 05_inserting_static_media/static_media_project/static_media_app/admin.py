from django.contrib import admin

# Register your models here.
# we need to tell the app that the models exist

from static_media_app.models import Topic, Webpage, AccessRecord
# the way that you register them is with:
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)

# we can create a super user with the following:
# python manage.py createsuperuser
# (default 10/17/22)

# go to http://127.0.0.1:8000//admin

# > pip install Faker
# in static_media_project folder create a new file

