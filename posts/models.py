from django.db import models
from django.urls import reverse
from datetime import datetime, date

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=225)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("home")


class Post(models.Model):
    title = models.CharField(max_length=225)
    author = models.CharField(max_length=225)
    category = models.CharField(max_length=225, default="coding")
    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    def __str__(self):
        return self.title + ' | '  + self.author

    def get_absolute_url(self):
        return reverse("home")
