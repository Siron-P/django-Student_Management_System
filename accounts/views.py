from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login

from .forms import SignupForm

def index(request):
    return render(request,"accounts/index.html")

def login(request):
    return render(request,"accounts/login.html")

def signup(request):
    return render(request,"accounts/signup.html")

# def signup(request):
#     if request.user.is_authenticated:
#         return redirect("accounts:signup")

#     if request.method == "POST":
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             auth_login(request,user)
#             return redirect("accounts:signup")
#         else:
#             form = SignupForm()

#         return render(request,"accounts/signup.html",{"form":form})