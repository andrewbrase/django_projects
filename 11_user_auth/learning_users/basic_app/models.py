from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):

    # this almost extends the class, 
    # do not inherit from the User class 
    # - it does not have multiple instances of this class
    user = models.OneToOneField(User)

    # additional attributes
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username

    # > pip install pillow