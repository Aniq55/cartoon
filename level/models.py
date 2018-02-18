from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
import datetime


class player(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=128)
    max_level = models.IntegerField(default=1)
    score = models.IntegerField(default=0)
    rank = models.IntegerField(default=0)
    timestamp = models.DateTimeField()

    def __str__(self):
        return self.name
