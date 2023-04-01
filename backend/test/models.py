
# Create your models here.
from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=80)
    age = models.IntegerField()


class Student(models.Model):
    Fname = models.CharField(max_length=80)
    Lname = models.CharField(max_length=80)
    age = models.IntegerField()
