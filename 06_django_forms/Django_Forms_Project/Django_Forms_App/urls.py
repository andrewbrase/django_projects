# The urls.py file you just created is specific for the Django_Forms_App application.
# We have to do some routing in the root directory Django_Forms_Project as well. This may 
# seem complicated, but for now, just follow the instructions below.

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]