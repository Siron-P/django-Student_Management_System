from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Course
from .forms import CourseForm

def admin_only(user):
    return user.is_authenticated and user.is_admin()

@login_required
def course_list(request):
    if not request.user.is_admin():
        return HttpResponseForbidden("You don't have access to this page.")
    courses = Course.objects.all().order_by("name")
    return render(request, "courses/course_list.html",{"courses" :courses})

@login_required
def add_course(request):
    if not request.user.is_admin():
        return HttpResponseForbidden("You don't have access to this page.")

    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("courses:course_list")
    else:
        form = CourseForm()

    return render(request,"courses/add_course.html",{"form":form})

@login_required
def edit_course(request, pk):
    if not request.user.is_admin():
        return HttpResponseForbidden("You don't have access to this page.")
    course = get_object_or_404(Course,pk=pk)
    if request.method== "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect("courses:course_list")
    else:
        form = CourseForm(instance=course)
    return render(request, "courses/course_form.html",{"form":form})

@login_required
def delete_course(request, pk):
    if not request.user.is_admin():
        return HttpResponseForbidden("You don't hve access to this page.")
    course = get_object_or_404(Course, pk=pk)
    if request.method == "POST":
        course.delete()
        return redirect("courses:course_list")
    return render(request, "courses/course_confirm_delete.html",{"course":course})
        

