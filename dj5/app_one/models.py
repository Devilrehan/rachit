from unicodedata import name
from django.db import models
from django.forms import CharField

# Create your models here.

class employee(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField()
    deppt_id = models.IntegerField()