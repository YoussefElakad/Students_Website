from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login
from .models import Login , student
from django import forms

class UpdateStudentForm(forms.ModelForm):
    class Meta:
        model=student
        fields='__all__'
# Create your views here.

def login(request):
    return render(request,'Login Page.html',{'lg':Login.objects.all()})

def home(request):
    return render(request,'Home Page.html')

def Add(request):

    if request.method=="POST":

        fn=request.POST.get('fname')
        ln=request.POST.get('lname')
        id=request.POST.get('id')
        db=request.POST.get('DB')
        gp=request.POST.get('gpa')
        ge=request.POST.get('gen')
        lev=request.POST.get('lev')
        stuts=request.POST.get('stuts')
        dep=request.POST.get('dep')
        em=request.POST.get('email')
        mob=request.POST.get('Mobile')

        data = student(fname=fn,lname=ln,id=id,BirthDate=db,gpa=gp,gender=ge,level=lev,status=stuts,depart=dep,email=em,phone=mob)
        data.save()
    return render(request,'Add student Page.html')

def Departement(request):
    return render(request,'Departement selection page.html',{'stu':student.objects.all()})

def Edit(request):
    return render(request,'Edit Page.html')

def Search(request):
    if request.method == 'GET':
        query = request.GET.get('search')
        
        try:
            students = student.objects.filter(name__contains=query)
            
            return render(request, 'Search page.html', {"stu": students})
        except:
            return render(request, 'Search page.html', {"stu": []})
    else:
        return render(request, 'Search page.html', {})

def View(request):
    return render(request,'View Students Page.html',{'stu':student.objects.all()})