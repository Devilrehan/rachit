from django.contrib import admin
from my_app.models import LoginDetails, Email, Phone

# Register your models here.

admin.site.register([LoginDetails, Email, Phone])