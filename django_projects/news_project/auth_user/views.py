from django.shortcuts import render

# Create your views here.
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import login, logout, authenticate

def login_view(request):

    context = {}

    return render(request, 'auth/login.html', context)