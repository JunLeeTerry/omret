from django.db import models

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


