from django.urls import path
from . import views

app_name = "teachers"

urlpatterns = [
    path("teacher_dashboard/",views.teacher_dashboard,name="teacher_dashboard"),
]