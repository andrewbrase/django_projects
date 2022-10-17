from django.db import models

class Topic(models.Model):
    top_name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)

# After you define the models, 
# Django will build out the SQL 
# database through a series of 
# commands

# (activate the env)
# in that project folder call 
# > python manage.py migrate
# > python manage.py makemigrations static_media_app
# > python manage.py migrate

# now our models should be connected to 
# a SQL database that Django has made for us
# and registered the changes to our app

