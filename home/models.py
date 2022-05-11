from django.db import models

# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=100)
    mobile = models.CharField(max_length=12)
    Description=models.CharField(max_length=122)

class signup(models.Model):
    Username = models.CharField(max_length=25)
    email = models.EmailField(max_length=100)
    password=models.CharField(max_length=122)

class task(models.Model):
    tasktitle = models.CharField(max_length=70)
    duedate = models.DateTimeField
    description=models.CharField(max_length=122)
    status = models.BooleanField
