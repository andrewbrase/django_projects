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

# The Members table is empty, we should add some members to it.
# In the next chapters you will learn how to make a user interface 
# that will take care of CRUD operations (Create, Read, Update, Delete), 
# but for now, let's write Python code directly in the Python interpreter 
# (Python shell) and add some members in our database, without the user interface.

# > py manage.py shell
# >>> from Django_Forms_app.models import Members
# Hit [enter] and write this to look at the empty Members table:
# >>> Members.objects.all()
# <QuerySet []>

# A QuerySet is a collection of data from a database.
# Read more about QuerySets in the Django QuerySet chapter.
# Add a record to the table, by executing these two lines:

# >>> Andrew = Members(firstname='Andrew', lastname='Brase')
# >>> Andrew.save()

# >>> Members.objects.all()
# <QuerySet [<Members: Members object (1)>]>
# >>> Members.objects.all().values()
# <QuerySet [{'id': 1, 'firstname': 'Andrew', 'lastname': 'Brase'}]>
# >>>

# Add Multiple Records
# You can add multiple records by making a list of Members obejcts, and execute .save() on each entry:
# >>> member1 = Members(firstname='Tobias', lastname='Refsnes')
# >>> member2 = Members(firstname='Linus', lastname='Refsnes')
# >>> member3 = Members(firstname='Lene', lastname='Refsnes')
# >>> member4 = Members(firstname='Stale', lastname='Refsnes')
# >>> members_list = [member1, member2, member3, member4]
# >>> for x in members_list:
# >>>   x.save()

