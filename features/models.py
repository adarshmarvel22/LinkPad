

from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

from django import forms

class Club(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)

    head=models.CharField(max_length=50,blank=True)

    def __str__(self):
        return self.name

class Hall_of_Fame(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)

    designation=models.CharField(max_length=100,blank=True)
    company=models.CharField(max_length=100,blank=True)
    contact=models.CharField(max_length=10,blank=True)
    pic= models.ImageField(upload_to='posts/',blank=True)

    def __str__(self):
        return f"{self.name} ({self.year})"

class Event(models.Model):
    name = models.CharField(max_length=40)
    date = models.DateField(default=datetime.now)
    # date = models.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    venue = models.CharField(max_length=200)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)

    desc=models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.name
    
def default_file_path():
    # Define the default file path here
    return 'profile_pics'

class Resources(models.Model):
    name = models.CharField(max_length=100,blank=True)
    file = models.FileField(upload_to='resources/',blank=True, default=default_file_path)
    
    description = models.TextField()
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Job(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE,blank=True)
    date_added = models.DateField(default=datetime.now)

    def __str__(self):
        return self.title