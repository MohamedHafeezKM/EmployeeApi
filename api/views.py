from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
# Create your views here.
from api.models import Employee
from api.serializers import EmployeeSerializer



class EmployeeView(ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer