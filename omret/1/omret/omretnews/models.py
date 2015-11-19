from django.db import models

# Create your models here.
class OmretNews(models.Model):
    author = models.CharField(max_length=50)
    up_votes = models.
