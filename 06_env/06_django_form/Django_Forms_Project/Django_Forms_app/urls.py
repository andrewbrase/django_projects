from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('add/addrecord/', views.addrecord, name='addrecord'),
    # So far we have made the user interface, and we point the URL to the view called addrecord, but we have not made the view yet.
    # Make sure you add the addrecord view in the in the Django_Forms_app/views.py file:

    # The "delete" link in the HTML table points to 127.0.0.1:8000/members/delete/ so we will add a path() 
    # function in the members/urls.py file, that points the url to the right location, with the ID as a parameter:
    path('delete/<int:id>', views.delete, name='delete'),

    # Add a path() function in the members/urls.py file, that points the url 127.0.0.1:8000/members/update/ 
    # to the right location, with the ID as a parameter:
    path('update/<int:id>', views.update, name='update'),

    # <!-- What Happens on Submit?
    # Did you notice the action attribute in the HTML form? 
    # The action attribute specifies where to send the form data, 
    # in this case the form data will be sent to:
    # updaterecord/{{ mymember.id }}, so we must add a path() 
    # function in the members/urls.py file that points to the right view: -->
    path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord')
    
]