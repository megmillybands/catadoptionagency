from django.db import models

GENDER = [
    ("F", "Female"),
    ("M", "Male"),
]

class Cat(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER)
    breed = models.CharField(max_length=50)
    description = models.TextField()