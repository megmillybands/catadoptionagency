from django.contrib import admin
from app.models import *
from accounts.models import *

admin.site.register(Cat)
admin.site.register(Bookmark)