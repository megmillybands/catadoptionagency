from django.contrib import admin
from django.urls import path, include
from app.views import *
from accounts.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("create_listing/", create_listing, name="create_listing"),
    path("<str:name>/", cat_details, name="cat_details"),
    path("<str:name>/edit_listing/", edit_listing, name="edit_listing"),
    path("<str:name>/delete/", delete_listing, name="delete_listing"),
    path("<str:name>/message/", send_message, name="send_message"),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)