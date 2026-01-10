from django.db import models
from django.contrib.auth.models import User

GENDER = [
    ("F", "Female"),
    ("M", "Male"),
]

class Cat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=20)
    gender = models.CharField(max_length=1, choices=GENDER)
    breed = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='cat_images/')

