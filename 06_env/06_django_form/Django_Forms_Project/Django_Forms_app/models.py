from django.db import models

# Create your models here.

class Members(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)

# py manage.py migrate

# > py manage.py makemigrations Django_Forms_app
    # Migrations for 'Django_Forms_app':
    # Django_Forms_app\migrations\0001_initial.py
    # - Create model Members

# > py manage.py migrate
    # Operations to perform:
    # Apply all migrations: Django_Forms_app, admin, auth, contenttypes, sessions
    # Running migrations:
    # Applying Django_Forms_app.0001_initial... OK