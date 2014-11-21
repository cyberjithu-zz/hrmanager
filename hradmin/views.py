from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from employee.models import EmployeeInfo
from django.forms.models import model_to_dict
# Create your views here.


@login_required(login_url='/')
def index(request):
    employee_objects = EmployeeInfo.objects.all()
    employee_objects = [model_to_dict(obj) for obj in employee_objects]
    return render(request, 'hradmin/hradmin.html', {'employee_objects': employee_objects})
