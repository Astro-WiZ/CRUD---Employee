from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length= 100)
    eID = models.IntegerField()
    designation = models.CharField(max_length=50, default= None)
    address = models.TextField()
    picture = models.ImageField()
    salary = models.FloatField()
    phone = models.IntegerField()