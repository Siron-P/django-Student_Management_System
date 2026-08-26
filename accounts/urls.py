from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

#auth_views just for removing confusion from line 1 and 4.

app_name = "accounts"

urlpatterns = [
    path("",views.index,name="index"),
    path("signup/",views.signup,name= "signup"),
    path("login/",auth_views.LoginView.as_view(template_name="accounts/login.html"),name="login"),
    path("logout/",auth_views.LogoutView.as_view(),name="logout")
]