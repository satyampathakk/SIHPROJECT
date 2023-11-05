# forms.py
from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['rollno','name','subject','quiz1', 'quiz2', 'quiz3', 'preend', 'endsem']
