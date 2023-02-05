from django.db import models

# Create your models here.
# science model
class Science(models.Model):
    name = models.CharField(max_length=100)
    

class Person(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=75)
    gender = models.BooleanField('f','m')
    science = models.ForeignKey('science', on_delete=models.CASCADE)
