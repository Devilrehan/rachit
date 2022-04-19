from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = 'home'),
    path('register', views.register, name = 'register'),
    path('show', views.show, name = 'datashow'),
    path('login', views.login, name = 'login'),
    path('logout', views.logout, name = 'logout'),
    path('posts', views.posts, name = 'posts'),
    path('post/<str:pk>', views.post, name = 'post'),
]
