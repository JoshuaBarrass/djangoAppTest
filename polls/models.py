from django.db import models
from django.db import models
from django.utils import timezone

import datetime
# Create your models here.
# Models are used to represent items in a database

class Question(models.Model):
    
    questionText = models.CharField(max_length=200)
    pubDate = models.DateTimeField('Date Published')
    
    def __str__(self):
        return self.questionText

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choiceText = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choiceText
    