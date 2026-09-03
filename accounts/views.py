from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib.auth.forms import AuthenticationForm

from .utils import redirect_after_login
from .forms import SignupForm
from .forms import PreregisterForm
from students.models import Student
from teachers.models import Teacher
from courses.models import Course

def index(request):
    return render(request, "accounts/index.html")

def login(request):
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

    context = {
        "total_students" : Student.objects.count(),
        "total_teachers" : Teacher.objects.count(),
        "total_courses" : Course.objects.count(),
        "pending_signups" : Student.objects.filter(user__isnull=True).count()+
                            Teacher.objects.filter(user__isnull=True).count(),
        "students" : Student.objects.select_related("course").order_by("student_id"),
        "teachers" : Teacher.objects.all().order_by("teacher_id"),
    }
    return render(request, "accounts/admin_dashboard.html",context)

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

    return render(request, "accounts/preregister.html", {
        "form": form,
        "courses" : Course.objects.all()
        })