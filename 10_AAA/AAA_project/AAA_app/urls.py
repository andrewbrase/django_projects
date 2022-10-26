from django.urls import path
from AAA_app import views

app_name = 'AAA_app'

urlpatterns = [
    path('signup/', views.signup, name='signup')
]