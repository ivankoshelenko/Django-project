import re
from email.utils import parseaddr

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def SignIn(request):
    if request.method =="POST":
        username = request.POST['username']
        if username == '':
            messages.info(request,'Неправильный username или пароль')
            return render(request,'signIn.html')
        password = request.POST['password']
        user = authenticate(request,username = username,password = password)
        if user is not None:
            login(request,user)
            return redirect('/home/')
        else:
            messages.info(request,'Неправильный username или пароль')
            return render(request,'signIn.html')
    return render(request, 'signIn.html')

@csrf_exempt
def SignUp(request):
        if request.method == "POST":
            name = request.POST['name']
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            if password1 == password2 and len(password1) >= 8 and checkEmail(email) and name != '':
                user = User.objects.create_user(name, email=email, password=password1)
                return redirect('signIn')
            else:
                return render(request, 'signUp.html')
        return render(request, 'signUp.html')

def checkEmail(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if (re.fullmatch(regex, email)):
        return True
    else:
        return False

def logOutUser(request):
    logout(request)
    return redirect('/sign/In')

