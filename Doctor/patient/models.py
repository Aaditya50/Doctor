from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    city = models.CharField(max_length=100)

    