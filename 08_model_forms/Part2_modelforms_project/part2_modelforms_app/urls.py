from django.urls import path
from part2_modelforms_app import views

urlpatterns = [
    path('users/', views.users, name='users'),
]