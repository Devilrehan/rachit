
from django.contrib import admin
from django.urls import path
from .views import EmployeeAPI

urlpatterns = [
    path('employee/',EmployeeAPI.as_view()),
]