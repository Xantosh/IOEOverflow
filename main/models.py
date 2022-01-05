from django.db import models

# Create your models here.
class Question(models.Model):
    text = models.CharField(max_length=1000)
    image = models.ImageField(null = True)
    upvote= models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)

