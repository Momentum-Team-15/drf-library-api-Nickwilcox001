from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    pass

class Book(models.Model):
    name = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    publish_date = models.DateField()
    genre = models.CharField(max_length=50)
    featured = models.BooleanField(default=False)

class Status(models.Model):
    desire = models.CharField(max_length=50)