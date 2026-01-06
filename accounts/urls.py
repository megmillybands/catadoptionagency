from django.urls import path, include
from accounts.views import *

urlpatterns = [
    path("signup/", signup_view, name="signup"),
    path("admin_signup/", admin_signup_view, name="admin_signup"),
    path("login/", login_view, name="login"),
    path("profile/", profile_view, name='profile'),
]