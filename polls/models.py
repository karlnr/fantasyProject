from django.db import models

# Create your models here.

'''
models – essentially, your database layout, with additional metadata.  
DRY Principle. The goal is to define your data model in one place and automatically derive things from it.
migrations are entirely derived from your models file, 
and are essentially a history that Django can roll through to update your database schema to match your current models.

small bit of model code gives Django a lot of information. With it, Django is able to:

Create a database schema (CREATE TABLE statements) for this app.
Create a Python database-access API for accessing Question and Choice objects.
'''

# polls/models.py¶
import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):
    def __str__(self):
        return self.question_text
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')  # optional first positional argument to a Field to designate a human-readable name

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    def __str__(self):
        return self.choice_text
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  #  tells Django each Choice is related to a single Question
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
