from django.db import models

# Create your models here.

class Employee(models.Model):
    name=models.CharField(max_length=50)
    options=(
        ('IT','IT'),
        ('HR','HR'),
        ('Front-End','Front-End'),
    )
    department=models.CharField(max_length=50,choices=options)
    mobile=models.IntegerField(max_length=10)
    salary=models.IntegerField()
    hr_user=models.CharField(max_length=50)