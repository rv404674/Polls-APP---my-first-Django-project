from django.db import models

import datetime
from django.utils import timezone

'''
Same in case of spring - Model contain class that will be embedded in the database
'''

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length = 200)

    pub_date = models.DateTimeField('date published')

    '''Return some text when this question is called'''
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()

        return now - datetime.timedelta(days=1)  <=self.pub_date <=now
        #return self.pub_date >= timezone.now() - \
        #  datetime.timedelta(days=1)

class Choice(models.Model):

    question = models.ForeignKey(Question,
                                 on_delete = models.CASCADE)

    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text