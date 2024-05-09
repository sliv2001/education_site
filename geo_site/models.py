from django.db import models
from django.contrib.auth.models import User

class Region(models.Model):
    name =  models.CharField(max_length=100)

class Country(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    capital = models.CharField(max_length=100)

class LearnRate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    repetition_number = models.IntegerField(default=0)
    tests_involve = models.IntegerField(default=0)
    tests_correct = models.IntegerField(default=0)
