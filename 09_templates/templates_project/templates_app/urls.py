from django.urls import path
from templates_app import views

# template tagging - set this to whatever the name of your app is
app_name = 'templates_app'

urlpatterns = [
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other'),
]