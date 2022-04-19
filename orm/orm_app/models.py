from platform import machine
from tkinter import CASCADE
from django.db import models
from django.forms import CharField

# Create your models here.
class Guest(models.Model):
    name = models.CharField(max_length=35)
    address = models.TextField()

    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=35)
    guest = models.OneToOneField(Guest, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=35)
    manager = models.CharField(max_length=35)
    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=35)
    deptt = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=35)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=35)
    subject = models.ManyToManyField(Subject)

    def __str__(self):
        return self.name