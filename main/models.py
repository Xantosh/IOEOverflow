from django.db import models
from django.conf import settings

# Create your models here.

class Question(models.Model):
    id = models.IntegerField(primary_key=True)
    text = models.CharField(max_length=1000)
    image = models.ImageField(null=True)
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)
    answer = models.ImageField(null=True)
    author = models.CharField(max_length=100,default="anon")
    upvoteList = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='upvote_count')
    downvoteList = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='downvote_count')


class QuestionComment(models.Model):
    post = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="comments")
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)


class TotalEntries(models.Model):
    value = models.IntegerField(default=0)
    name= models.CharField(max_length=10)


