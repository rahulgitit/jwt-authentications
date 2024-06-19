from django.db import models

# Create your models here.
class testdb(models.Model):
    name= models.CharField(max_length=100)
    rollno = models.IntegerField()
    city = models.CharField(max_length=100)