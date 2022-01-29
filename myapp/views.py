from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth.models import User, auth
from django.contrib import messages

def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        return render(request, 'index.html', {'username':username})
    else:
        return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'email already exits!')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'username already exits!')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password, email=email)
                user.save();
                return redirect('login')
        else:
            messages.info(request, 'password do not same, please enter same password')
            return redirect('register')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid username or password') 
            return redirect('login')
    else:  
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')