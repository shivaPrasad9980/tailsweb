from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
from .models import Students
from .forms import StudentForm


# Create your views here.
def logIn(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username,password = password)
        if user is not None:
            user(request,login)
    return render(request,'login.html')

def home(request):
    students = Students.objects.all()
    return render(request,'home.html',{'students':students})

def logOut(request):
    logout(request)
    return redirect('/')

def add_student(request):
    form = StudentForm(request.POST)
    if form.is_valid():
        form.save()
    form = StudentForm()
    return render(request,'add_student.html',{'form':form})

def deleteStudent(request,id):
    stu = Students.objects.get(id=id)
    stu.delete()
    return redirect('/')

def updateStudent(request,id):
    stu = Students.objects.get(id=id)
    form = StudentForm(instance=stu)
    if request.method == "POST":
        form = StudentForm(request.POST,instance=stu)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'update.html',{"form":form})