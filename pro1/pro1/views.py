from multiprocessing import context
from unicodedata import name
from django.shortcuts import render


from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def show(request):
    name = request.GET['name']
    password = request.GET['password']

    context = {
        'username': name,
        'pass'    : password
    }
    return render(request, 'show.html', context)

