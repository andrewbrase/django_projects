from django.db import models

# Create your models here.

class foodItem(models.Model):
    food_name = models.CharField(max_length=25)
    quantity = models.IntegerField()

# 32”, 43”, 55” 65” 75” and 85” 
TV_SCREEN_SIZES = [
    (32, "32''"),
    (43, "43''"),
    (55, "55''"),
    (65, "65''"),
    (75, "75''"),
    (85, "85''"),
]

class tv(models.Model):
    screen_size = models.CharField(max_length=25, choices=TV_SCREEN_SIZES)
    quantity = models.IntegerField()