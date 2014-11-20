from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login as authlogin, authenticate
from django.contrib.auth.models import User, Group
from employee.models import EmployeeInfo
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method == "GET":
        return render(request, "index.html", {'error': ''})
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                adming_group = Group.objects.get(name="admin")
                if adming_group in user.groups.all():
                    authlogin(request, user)
                    employee_objects = EmployeeInfo.objects.all()
                    employee_objects = [model_to_dict(obj) for obj in employee_objects]
                    return HttpResponseRedirect('hradmin/', {"employee_objects": employee_objects})
                else:
                    return HttpResponse("haseeb failed 3")
            else:
                return HttpResponse("haseeb failed 1")
        else:
            msg = 'Username or password incorrect'
            return render(request, "index.html", {'error': msg})
