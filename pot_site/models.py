from django.db import models
from datetime import datetime

# Create your models here.
class Img_data(models.Model):
    title = models.CharField(max_length=10000)
    img_url = models.TextField(max_length=2048,blank=True)
    posted_at = models.DateTimeField(default=datetime.now,blank = True)

class LoginData(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    

class SignupData(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=254,default="")
    password = models.CharField(max_length=100)
    gender = models.CharField(max_length=100,default="")
    dob = models.CharField(max_length=100)
