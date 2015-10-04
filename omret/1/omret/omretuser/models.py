from django.db import models
from omret.logret import models as logret_models

# Create your models here.

##------the part of the omret user-----------
##------user profile table----------
class UserProfile(models.Model):
    user = models.OneToOneField(logret_models.User)
    realname = models.CharField(max_length=30)
    sex = models.BooleanField()
    birthday = models.DateField(auto_now=False,auto_now_add=False)
    signature = models.TextField(max_length=120)
    resume = models.TextField()

    def __str__(self):
        return self.name

##------user relationship------
class UserRelationship(models.Model):
    user =
    user_follow =
    user_followers =
