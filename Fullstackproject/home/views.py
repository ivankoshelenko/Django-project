from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

@login_required(login_url='signIn')
def homepage(request):
    return render(request,'home.html')