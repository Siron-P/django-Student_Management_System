from django.urls import path
from . import views

app_name = "courses"

urlpatterns = [
    path("",views.course_list,name="course_list"),
    path("add/",views.add_course,name="add_course"),
    path("<int:pk>/edit/",views.edit_course, name="edit_course"),
    path("<int:pk>/delete/",views.delete_course,name="delete_course"),
]