from django.db import models
from django.contrib.auth.models import User
from app.models import *

class Bookmark(models.Model):
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('cat', 'user')