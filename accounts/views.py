from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from .forms import SignupForm

def home(request):
    return render(request,"accounts/home.html")

def signup(request):
    if request.user.is_authenticated:
        return redirect("accounts:home")

    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect("accounts:home")
        else:
            form = SignupForm()

        return render(request,"accounts/signup.html",{"form":form})