from django.db import models
from django import forms
from django.contrib.auth.models import User
# Create your models here.
class Student(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=1000)
    rollno=models.IntegerField()
    subject=models.CharField(max_length=1000)
    quiz1=models.IntegerField(null=True,blank=True, default=None)
    quiz2=models.IntegerField(null=True,blank=True, default=None)
    quiz3=models.IntegerField(null=True,blank=True, default=None)
    preend=models.IntegerField(null=True,blank=True, default=None)
    endsem=models.IntegerField(null=True,blank=True, default=0)
    predict=models.FloatField(null=True, blank=True, default=0)
    slow_learner=models.CharField(max_length=50,default='Fast Learner')
    mentor=models.IntegerField(null=True,blank=True, default=0)
    def __str__(self):
        return self.name



