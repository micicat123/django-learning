from tkinter import Widget
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)

    profilePicture = models.ImageField(upload_to='profilePictures', blank=True)

    def __str__(self):
        return self.user.username

class Topic(models.Model):
    top_name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=255)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.DO_NOTHING)
    date = models.DateField()

    def __str__(self):
        return str(self.date)