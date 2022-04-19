from django.contrib import admin
from django.urls import path
from .views import QuickshopAPI

urlpatterns = [
    path('quickshop/', QuickshopAPI.as_view()),
]