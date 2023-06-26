from django.db import models


# Create your models here.

class Food(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    price = models.IntegerField(max_length=200)
    category = models.CharField(max_length=200)
    image = models.ImageField()

