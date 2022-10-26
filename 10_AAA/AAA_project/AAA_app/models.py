from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Account(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=70)
    password = models.CharField(max_length=200)

    # ?? You should create a ModelForm (docs), which has a field that uses the PasswordInput widget from the forms library.
    # you would use a custom validator, specifically MinLengthValidator for min length on password
