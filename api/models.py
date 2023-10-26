from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UploadImage(models.Model):
    image  = models.ImageField(upload_to='uploads/')
class FileUpload(models.Model):
    file = models.FileField(upload_to='uploads/')

class Employee(models.Model):
    emp_id = models.ForeignKey(User,on_delete=models.CASCADE)
    emp_name = models.CharField(max_length=100)
    emp_salary = models.FloatField()
    em_address = models.CharField(max_length=256)
    age = models.IntegerField()
    dob = models.DateField()

