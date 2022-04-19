import email
from django.forms import PasswordInput
from django.shortcuts import render ,redirect
from django.contrib.auth.models import auth, user
from django.contrib import messages


# Create your views here.

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        username = request . POST = ['name']
        useremail = request . POST = ['email']
        userpassword = request . POST = ['password']
        userpassword2 = request . POST = ['password2']

        if  userpassword == userpassword2:
            if user.objects.filter(username=username).exists():
                messages.info(request, 'username already exists')
                return redirect("")
            
            elif user.objects.filter(email=useremail).exists():
                messages.info(request, 'Email already in use')
                return redirect("")

            else:
                newuser = user.objects.create_user(name = username, email = useremail, password = userpassword)
                newuser.save()
                return redirect("show")
        else:
            messages.info(request, 'userpassword does not match') 
            return redirect("") 
    return render(request, 'resister.html')

def show(request):
    users = user.objects.all()
    return render(request, 'show.html', {'deatails': users})

def login(request):
    if request.method == 'POST':
        username = request.post['name']
        userpassword = request.post['Password']

        user = auth.authenticate(name = username, password = userpassword)
       
        if user is not None:
           return redirect('show')
        else:
            messages.info(request, "Invalid Credentials")
            return redirect('home')

    return render(request, 'login.html')

