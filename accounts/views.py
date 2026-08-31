from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib.auth.forms import AuthenticationForm

from .utils import redirect_after_login
from .forms import SignupForm
from .forms import PreregisterForm

def index(request):
    if request.user.is_authenticated:
        return redirect(redirect_after_login(request.user))
    return render(request, "accounts/index.html")

def login(request):
    if request.user.is_authenticated:
        return redirect(redirect_after_login(request.user))
    
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request,user)
            return redirect(redirect_after_login(user))
    else:
        form = AuthenticationForm()

    return render(request, "accounts/login.html",{"form":form})

def signup(request):
    if request.user.is_authenticated:
        return redirect(redirect_after_login(request.user))

    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            return redirect(redirect_after_login(user))
    else:
        form = SignupForm()

    return render(request,"accounts/signup.html",{"form":form})

@login_required
def admin_dashboard(request):
    if not request.user.is_admin():
        return HttpResponseForbidden("You don't have access to this page.")
    return render(request, "accounts/admin_dashboard.html")

@login_required
def preregister(request):
    if not request.user.is_admin():
        return HttpResponseForbidden("You don't have access to this page.")

    if request.method == "POST":
        form = PreregisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("accounts:preregister")
    else:
        form = PreregisterForm()

    return render(request, "accounts/preregister.html", {"form": form})