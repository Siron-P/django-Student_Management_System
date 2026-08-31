from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

#auth_views just for removing confusion from line 1 and 4.

app_name = "accounts"

urlpatterns = [
    path("",views.index,name="index"),
    path("signup/",views.signup,name= "signup"),
    path("login/",views.login,name="login"),
    path("logout/",auth_views.LogoutView.as_view(),name="logout"),
    path("admin-dashboard/",views.admin_dashboard,name="admin_dashboard"),
    path("preregister/",views.preregister,name="preregister")
]