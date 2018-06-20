from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
from django.urls import reverse


class Answer(models.Model):
    author = models.CharField(max_length=20)
    created_date = models.DateTimeField(default=datetime.now())
    text = models.TextField(default="")

    def __str__(self):
        return str(self.author) + str(self.created_date)


class Topic(models.Model):
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=datetime.now())
    visits_no = models.IntegerField(default=0)
    answers_no = models.IntegerField(default=0)
    last_answer_date = models.DateTimeField(blank=True, null=True)
    last_answer_author = models.CharField(max_length=30, default="Noone")
    text = models.TextField(default="")
    answers = models.ManyToManyField(Answer)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('forum:detail', kwargs={'slug': self.title})
