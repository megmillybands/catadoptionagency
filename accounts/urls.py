from django.urls import path
from accounts.views import *

urlpatterns = [
    path("signup/", signup_view, name="signup"),
    path("login/", login_view, name="login"),
    path("profile/", profile_view, name='profile'),
    path("profile/edit/", edit_account, name="edit_profile"),
    path("profile/edit/change_password/", change_password, name="change_password"),
    path("profile/delete/", delete_account, name="delete_account"),
]