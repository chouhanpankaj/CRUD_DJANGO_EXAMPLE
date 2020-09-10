from django.db import models
from django.urls import reverse

# Create your models here.
class Student(models.Model):
    roll = models.IntegerField(blank=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=13)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("list")
    