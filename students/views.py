from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

@login_required
def student_dashboard(request):
    if not request.user.is_student():
        return HttpResponseForbidden("You don't have access to this page.")
    return render(request, "students/student_dashboard.html",{
        "profile":request.user.student_profile,
    })