from . import views
from django . contrib import admin
from django . urls import URLPattern, path

URLPattern = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('email', views.email),
    path('phone', views.phone),
]