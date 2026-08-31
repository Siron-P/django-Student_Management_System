from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

@login_required
def teacher_dashboard(request):
    if not request.user.is_teacher():
        return HttpResponseForbidden("You don't have access to this page.")
    return render(request, "teachers/teacher_dashboard.html",{
        "profile":request.user.teacher_profile,
    })