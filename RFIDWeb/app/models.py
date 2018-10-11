"""
Definition of models.
"""

from django.db import models
from django.utils import timezone

# Create your models here.

class rawdata(models.Model):
    text = models.TextField()

class userlist(models.Model):
    in_out = (('in','In'),('out','Out'))
    entrydate = models.DateField(default='django.utils.timezone.now()')
    username = models.CharField(max_length=30)
    scan_id = models.CharField(max_length=30, primary_key=True)
    access = models.CharField(max_length=30)
    image = models.ImageField(upload_to='img')
    area = models.CharField(max_length=30, default="None")
    status = models.CharField(max_length=3,choices=in_out,default='in')
    def __str__(self):
        return self.username
    
class accesslog(models.Model):
    entrydate = models.DateTimeField(default='django.utils.timezone.now()')
    area = models.CharField(max_length=30)
    scan_id = models.CharField(max_length=30)
    scan_type = models.CharField(max_length=30)
    username = models.ForeignKey(userlist, on_delete=models.SET_DEFAULT, default="default")
    action = models.CharField(max_length=30)
    def __str__(self):
        return self.scan_id + self.scan_type

class scanners(models.Model):
    in_out = (('in','In'),('out','Out'))
    clientid = models.CharField(max_length=30, primary_key=True)
    area = models.CharField(max_length=30)
    door = models.CharField(max_length=30)
    direction = models.CharField(max_length=3,choices=in_out,default='in')
    latch = models.BooleanField(default = False)
    description = models.CharField(max_length=30)
    online = models.BooleanField(default = False)
    def __str__(self):
        return self.clientid