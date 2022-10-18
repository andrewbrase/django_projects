from django.db import models

# The model provides data from the database.
# In Django, the data is delivered as an Object Relational Mapping (ORM),
# which is a technique designed to make it easier to work with databases.
# The most common way to extract data from a database is SQL. One problem 
# with SQL is that you have to have a pretty good understanding of the 
# database structure to be able to work with it.
# Django, with ORM, makes it easier to communicate with the database, 
# without having to write complex SQL statements.

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

# how to look at that database - 
# create some test data with some shell commands
# using python at the shell we can interact with
# our database

# > python manage.py shell
# this will open up an interactive shell

# >>> from static_media_app.models import Topic
# >>> print(Topic.objects.all())
# <QuerySet []>
# >>>

# you'll get nothing back from the first time,
# lets create something

# (making a new Topic)
# >>> t = Topic(top_name="Social Network")
# >>> t.save()
# ( .save() is inherited from the model.Models class)

# if we try to print out all of the topic objects we now get this
# >>> print(Topic.objects.all())
# <QuerySet [<Topic: Social Network>]>
# >>>
# >>> quit()

# so far we've created models and the database behind it
# we actually used shell commands to add something
# we're not going to be using the shell everytime we want to add, view the database
# in order to have more convieneance we'll use the admin interface

