from django.db import models
from omret.logret import models as logret_models

# Create your models here.

##------the part of the omret user-----------
##------user profile table----------
class UserProfile(models.Model):
    user = models.OneToOneField(logret_models.User)
    realname = models.CharField

