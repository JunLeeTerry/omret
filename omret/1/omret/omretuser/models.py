from django.db import models
from omret.logreg import models as logreg_models

# Create your models here.

##------the part of the omret user-----------
##------user profile table----------
class UserProfile(models.Model):
    user = models.OneToOneField(logreg_models.User)
    realname = models.CharField(max_length=50)
    sex = models.CharField(choices=(('F','Female'),('M','Male')),max_length=5)
    birthday = models.DateField(auto_now=False,auto_now_add=False)
    #birthday = models.CharField(max_length=30)
    signature = models.TextField(max_length=120)
    resume = models.TextField()

    def __str__(self):
        return self.user.name

##----user head img table------
class UserHeadImg(models.Model):
    user = models.OneToOneField(logreg_models.User)
    url = models.CharField(max_length=3000)

##------user relationship------
#class UserRelationship(models.Model):
#    user = models.ForeignKey(logreg_models.User)
#    user_follow = models.IntegerField()
#    user_followers = models.IntegerField()
#
#    def __str__(self):
#        return self.user.name + 'follow: ' + user_follow + 'followers: ' + user_followers
