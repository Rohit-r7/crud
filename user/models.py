from django.db import models


# Create your models here.

class Userdetails(models.Model):
    name = models.CharField(max_length=20,default='')

class Authentication(models.Model):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    role = models.CharField(max_length=10,default="user") 
    user = models.ForeignKey(Userdetails,on_delete=models.CASCADE)

class Quotes(models.Model):
    user = models.ForeignKey(Userdetails,on_delete=models.CASCADE,default='')
    status = models.CharField(max_length=50,default='pending')
    quote = models.CharField(max_length=1000)



