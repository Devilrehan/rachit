from urllib import response
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to my site")


def about(request):
    return HttpResponse("This is the about section.<br> i am rachit verma.<br> i am from kanpur<br> This is my first django project</b>")