from django.db import models

# Create your models here.

class LoginDetails(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=15)


class Email(models.Model):
    sender_mail = models.CharField(max_length=60)
    subject = models.CharField(max_length=150)
    body = models.TextField()


class Phone(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=30)
    Phone = models.IntegerField()