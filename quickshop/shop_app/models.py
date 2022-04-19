from itertools import product
from django.db import models


# Create your models here.
class Quickshop(models.Model):
    product = models.CharField(max_length=60)
    price = models.IntegerField()
    description = models.TextField()
    
    

def __str__(self):
    return self.product