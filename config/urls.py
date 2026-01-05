from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from app.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
]