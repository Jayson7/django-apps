from django.shortcuts import render, redirect
from members import views
from members.views import *
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    if User.is_authenticated:
        return render(request, 'index.html')
    else:
        return redirect(request, 'login.html')    
    return render(request, 'index.html')

