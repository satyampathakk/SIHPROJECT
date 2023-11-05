from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,JsonResponse
from .models import *
from django.core import serializers
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from .forms import StudentForm
from .predict import Predict

# Create your views here.

def index (request):
    return render(request,'index.html')

@login_required
def show(request):
    user=request.user
    student = Student.objects.filter(user=user)
    context={}
    Predict()
    context['student']=student
    return render (request,'show.html',context)

def register(request):
    if request.method=='POST':
        user=request.POST['username']
        password=request.POST['password']
        err=''
        if User.objects.filter(username=user).exists():
            return render(request,'register.html',{ 'err':'username already exists'})

        user=User.objects.create_user(username=user,email="",password=password)
        user.save()
        return redirect('login')
    return render(request,'register.html')

def login(request):
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user=auth.authenticate(username=username,password=password)
        if user is not None:

            auth.login(request,user)
            return redirect('dashboard')
        else:
            messages.info(request,"encorrect user name or password")
            return redirect ('login')
    return render (request,'login.html')

@login_required
def dashboard(request):
    return render(request,'dashboard.html')

@login_required
def logout(request):
    auth.logout(request)
    return redirect('login')

@login_required
def submit(request):
    student=Student()
    if request.method == 'POST':
        try:
            student.rollno = request.POST['rollno']
            student.name=request.POST['name']
            student.subject = request.POST['subject']
            student.quiz1 = request.POST['quiz1']
            student.quiz2 = request.POST['quiz2']
            student.quiz3 = request.POST['quiz3']
            student.preend = request.POST['preend']
            student.endsem = request.POST['endsem']
            student.mentor=request.POST['mentor']
            student.user=request.user

            student.save()
            return render(request, 'show', )
        except Exception as e:
            return render(request, 'submit.html', { 'error_message': str(e)})
    else:
        return render(request, 'submit.html')
    return render(request, 'submit.html')

        
    # No use for now
def retrieve(request):
    student = Student.objects.all()
    data=serializers.serialize('json',student)
    return JsonResponse(data,safe=False)

@login_required
def delete(request,id):
    if request.method=='POST':

        Student.objects.filter(pk=id).delete()
    return redirect('show')


@login_required
def update(request, id):
    student = get_object_or_404(Student, pk=id)

    if request.method == 'POST':
        try:
            student.rollno = request.POST['rollno']
            student.name=request.POST['name']
            student.subject = request.POST['subject']
            student.quiz1 = request.POST['quiz1']
            student.quiz2 = request.POST['quiz2']
            student.quiz3 = request.POST['quiz3']
            student.preend = request.POST['preend']
            student.endsem = request.POST['endsem']
            student.mentor=request.POST['mentor']

            student.save()
            return render(request, 'show', {'stud': student})
        except Exception as e:
            return render(request, 'update.html', {'stud': student, 'error_message': str(e)})
    else:
        return render(request, 'update.html', {'stud': student})


    return render(request, 'update.html', { 'stud': student})

@login_required
def particular(request, rollno):
    students = Student.objects.filter(rollno=rollno)  
    if students.exists():
        student=students
        
    else :
        student = None

    return render(request, 'particular.html', {'studs': student})

def search(request):
    rollno=request.POST['rollno']
    name=request.POST['name']
    student=Student.objects.filter(rollno=rollno,name=name)
    return render(request,'student.html',{'student':student})

def forgot(request):
    pass





    















































