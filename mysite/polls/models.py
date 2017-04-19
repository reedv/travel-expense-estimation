from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible  # for supporting python2

import datetime

# Create your models here.
# Essentially, your database layout, with additional metadata.
# Each model is represented by a class that subclasses django.db.models.Model.
# Each model has a number of class variables, each of which represents a database field in the model.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published') # set a human-readable name for this field

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        """
        return whether this question was published with 1 day
        """
        return timezone.now() - datetime.timedelta(days=1) <= self.pub_date <= timezone.now()
    # set some method properties (for Question admin's ModelAdmin list_display)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # tells django that each choice is related to a single Question, question
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
