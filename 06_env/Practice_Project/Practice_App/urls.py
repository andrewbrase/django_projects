from django.urls import re_path
from Practice_App import views
# from django.urls import path

urlpatterns = [
    re_path(r'^$', views.users, name='users'),
]