import datetime

from datetime import timezone
from django.db import models

# Create your models here.
class Question(models.Model):
    questions_text = models.CharField(max_length= 200 )
    pub_date= models.DateField('date published')

    def __str__(self):
        return self.questions_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length= 200)
    vote = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text