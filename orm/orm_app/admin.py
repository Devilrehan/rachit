from django.contrib import admin
from .models import *\

# Register your models here.
admin.site.register([Guest, Room, Department, Employee, Subject, Student])
