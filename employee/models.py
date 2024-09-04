from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Employee(models.Model):
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length= 100)
    eID = models.IntegerField()
    designation = models.CharField(max_length=50, default= None)
    address = models.TextField()
    picture = models.ImageField()
    salary = models.FloatField()
    phone = models.IntegerField()