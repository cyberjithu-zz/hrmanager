from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login as authlogin, authenticate, logout as authlogout
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from employee.models import EmployeeInfo
from hradmin.models import HrAdminInfo


def login(request):
    adming_group = Group.objects.get(name="admin")
    if request.method == "GET":
        if request.user.is_authenticated():
            if adming_group in request.user.groups.all():
                return HttpResponseRedirect('hradmin/')
            else:
                return HttpResponseRedirect('employee/')
        else:
            return render(request, "index.html", {'error': ''})
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                if adming_group in user.groups.all():
                    authlogin(request, user)
                    
                    return HttpResponseRedirect('hradmin/')
                else:
                    authlogin(request, user)
                    return HttpResponseRedirect('employee/')
            else:
                return HttpResponse("haseeb failed 1")
        else:
            msg = 'Username or password incorrect'
            return render(request, "index.html", {'error': msg})


def logout(request):
    authlogout(request)
    return HttpResponseRedirect('/')
