from django.db import models

# Create your models here.

class foodItem(models.Model):
    item_name = models.CharField(max_length=25)
    quantity = models.IntegerField()

# 32”, 43”, 55” 65” 75” and 85” 
TV_SCREEN_SIZES = [
    ("32 inch tv", "32''"),
    ("43 inch tv", "43''"),
    ("55 inch tv", "55''"),
    ("65 inch tv", "65''"),
    ("75 inch tv", "75''"),
    ("85 inch tv", "85''"),
]

class tv(models.Model):
    item_name = models.CharField(max_length=25, choices=TV_SCREEN_SIZES)
    quantity = models.IntegerField()