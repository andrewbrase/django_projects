from django.contrib import admin
from Practice_App.models import User
# Register your models here.
admin.site.register(User)
# > py manage.py createsuperuser