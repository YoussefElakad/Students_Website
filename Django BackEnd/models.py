from django.db import models

# Create your models here.

class student(models.Model):
    First = 'First' 
    Second = 'Second'
    Third = 'Third'
    Fourth ='Fourth'
    LEVEL_CHOICES = (
    (First, '1'),
    (Second, '2'),
    (Third, '3'),
    (Fourth, '4'),
    )
    Active = 'Active'
    inactive = 'inactive'
    STATUS_CHOICES = (
    (Active, 'Active'),
    (inactive, 'Inactive'),
    )
    CS = 'CS' 
    AI ='AI'
    IS = 'IS'
    IT = 'IT'

    DEPART_CHOICES = (
    (CS, 'Computer Sceince'),
    (AI, 'Artificial Intelligence'),
    (IS, 'Information System'),
    (IT, 'Information Technology'),
    )

    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    id=models.CharField(primary_key=True, max_length=50)
    BirthDate=models.DateField(auto_now=False, auto_now_add=False)
    gpa=models.DecimalField(max_digits=4,decimal_places=3)
    gender = models.CharField(max_length = 8)
    level = models.CharField(max_length = 10, choices = LEVEL_CHOICES, default = First)
    status = models.CharField(max_length = 10, choices = STATUS_CHOICES, default = First)
    depart = models.CharField(max_length = 50, choices = DEPART_CHOICES, default = IT)
    email = models.EmailField(max_length=90)
    phone = models.CharField(max_length=15)

class Login(models.Model):
    Email = models.EmailField(primary_key=True,max_length=60)
    Password = models.CharField(max_length=10)