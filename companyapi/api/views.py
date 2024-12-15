from django.shortcuts import render
from rest_framework import viewsets
from api.models import company, Employee
from api.serializers import CompanySerializers, EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = company.objects.all()
    serializer_class = CompanySerializers
    
    @action(detail=True,methods=['get'])
    def employees(self,request,pk=None): 
        company_instance=company.objects.get(pk=pk)
        # company_instance=self.get_object()
        emps=Employee.objects.filter(company=company_instance)
        emps_serializer=EmployeeSerializer(emps,many=True,context={'request':request})
        return Response(emps_serializer.data)
    
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
# Create your views here.
