from unicodedata import name
from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    bio = models.CharField(max_length=500)