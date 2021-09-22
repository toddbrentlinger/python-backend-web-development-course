from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Feature

# Create your views here.
def index(request):
    # feature1 = Feature('Fast', 'Our service is very quick', 0)
    # feature2 = Feature('Reliable', 'Our service is very reliable', 1)
    # feature3 = Feature('Easy to Use', 'Our service is easy to use', 2)
    # feature4 = Feature('Affordable', 'Our service is affordable', 3)
    features = Feature.objects.all()
    return render(request, 'index.html', {'features': features})

def contact(request):
    return HttpResponse('<h1>Contact Page</h1>')

def counter(request):
    context = {
        'amount': len(request.POST['text'].split())
    }
    return render(request, 'counter.html', context)

def register(request):
    # Check request method
    if request.method != 'POST':
        return render(request, 'register.html')
    
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    # Check passwords match
    if password != password2:
        messages.info(request, 'Passwords Do Not Match')
        return redirect('register')

    # Check email
    if User.objects.filter(email=email).exists():
        messages.info(request, 'Email Already Used')
        return redirect('register')

    # Check username
    if User.objects.filter(username=username).exists():
        messages.info(request, 'Username Already Used')
        return redirect('register')

    # Reach here if passwords match and both email and username are available
    user = User.objects.create_user(username=username, email=email, password=password)
    user.save()
    return redirect('login')

def login(request):
    # Check request method
    if request.method != 'POST':
        return render(request, 'login.html')

    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)

    # Check User
    if user is None:
        messages.info(request, 'Credentials Invalid')
        return redirect('login')

    # Reach here if User credentials has been authenticated    
    auth.login(request, user)
    return redirect('/')

def logout(request):
    auth.logout(request)
    return redirect('/')