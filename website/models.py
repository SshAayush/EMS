from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class UsersList(models.Model):
    uid = models.CharField(max_length = 50)
    fname = models.CharField(max_length = 50)
    lname = models.CharField(max_length = 50)
    uname = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 200)
    password = models.CharField(max_length = 100)
    starttime = models.DateTimeField(auto_now_add=True)
    profile_url = models.CharField(max_length = 1000)
    
    def __str__(self):
        return self.fname + ' ' + self.lname
    
class Staff(models.Model):
    s_fname = models.CharField(max_length = 100)
    s_lname = models.CharField(max_length=100)
    s_Email = models.EmailField(max_length=50)
    s_status = models.BooleanField(default = False)
    s_starttime = models.DateTimeField(auto_now_add=False)
    s_endtime = models.DateTimeField(auto_now_add=False)
    
    def __str__(self):
        return self.s_fname + ' ' + self.s_lname
    
class Time(models.Model):
    clockin = models.DateTimeField(auto_now_add = False)
    clockout = models.DateTimeField(auto_now_add = False)