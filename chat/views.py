from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from employee.models import EmployeeInfo
from hradmin.models import HrAdminInfo
from django.forms.models import model_to_dict

# from django.contrib.auth.models import User


@login_required(login_url='/')
def index(request):
    employees = EmployeeInfo.objects.all()
    admins = HrAdminInfo.objects.all()
    context = {'employees': employees, 'admins': admins}
    return render(request, 'chat/index.html', context)
