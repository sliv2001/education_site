"""
The module contains description of models, used in geo_site app.
"""
from django.db import models
from django.contrib.auth.models import User

class Region(models.Model):
    """
    Region of the world where the country is situated.
    """
    name =  models.CharField(max_length=100)

class Country(models.Model):
    """
    Country description: region where it is situated, name and the capital.
    """
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    capital = models.CharField(max_length=100)

class LearnRate(models.Model):
    """
    Statistics of learning for each country and each user.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    repetition_number = models.IntegerField(default=0)
    tests_involve = models.IntegerField(default=0)
    tests_correct = models.IntegerField(default=0)
