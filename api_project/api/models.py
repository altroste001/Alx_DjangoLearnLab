from django.db import models

title = models.CharField(max_length=200)
author = models.CharField(max_length=100)


def __str__(self):
    return self.title

# Create your models here.
