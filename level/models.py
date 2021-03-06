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


class level(models.Model):
    l_number = models.IntegerField()
    image1 = models.ImageField(upload_to = 'images',default='images/level1.jpg')
    image2 = models.ImageField(upload_to = 'images',default='images/level1.jpg')
    text = models.TextField()
    answer = models.CharField(max_length=200)
    numuser = models.IntegerField(default=0)
    accuracy = models.FloatField(default=0)
    wrong = models.IntegerField(default=0)

    def __str__(self):
        return self.text

class Notif(models.Model):
    text = models.CharField(max_length=200)
    date = models.DateTimeField(datetime.datetime.now())

    def __str__(self):
        return self.text


class UserProfile(models.Model):
    user = models.OneToOneField(User)

    def __str__(self):
        return self.user.username


admin.site.register(player)
admin.site.register(level)
admin.site.register(UserProfile)


#@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Player.objects.create(user=instance)
        instance.player.save()

