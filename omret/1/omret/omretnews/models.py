from django.db import models
from omret.logreg import models as logreg_models

# Create your models here.
class OmretNews(models.Model):
    author = models.CharField(max_length=50)
    up_votes = models.DecimalField(max_digits=19,decimal_places=10)
    down_votes = models.DecimalField(max_digits=19,decimal_places=10)
    subtime = models.DateTimeField(auto_now_add=True)
    #subday = models.DateField(auto_now_add=True)
    topic = models.ForeignKey('Topic')
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=1000)

class Topic(models.Model):
    name = models.CharField(max_length=20)
    color = models.CharField(max_length=10)
    def __str__(self):
        return self.name

class NewComments(models.Model):
    article_id = models.ForeignKey('OmretNews')
    #comments under the commnent
    comment_id = models.ForeignKey('NewComments')
    comment_content = models.CharField(max_length=200)
    comment_time = models.DateTimeField(auto_now_add=True)
    comment_user = models.OneToOneField(logreg_models.User)
