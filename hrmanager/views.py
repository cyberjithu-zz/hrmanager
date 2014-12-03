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
                    try:
                        current_user = HrAdminInfo.objects.filter(user=user)[0]
                        current_user.active_flag = True
                        current_user.save()
                        return HttpResponseRedirect('hradmin/')
                    except Exception as e:
                        return HttpResponse('Something went wrong in admin login...!' + '\n' + str(e))
                else:
                    authlogin(request, user)
                    try:
                        current_user = EmployeeInfo.objects.filter(user=user)[0]
                        current_user.active_flag = True
                        current_user.save()
                        return HttpResponseRedirect('employee/')
                    except Exception as e:
                        return HttpResponse('Something went wrong in employee login...!' + '\n' + str(e))
            else:
                return HttpResponse("User is not active")
        else:
            msg = 'Username or password incorrect'
            return render(request, "index.html", {'error': msg})


def logout(request):
    user = request.user
    adming_group = Group.objects.get(name="admin")
    try:
        if adming_group in user.groups.all():
            current_user = HrAdminInfo.objects.filter(user=user)[0]
        else:
            current_user = EmployeeInfo.objects.filter(user=user)[0]
        if current_user:
            current_user.active_flag = False
            current_user.save()
        authlogout(request)
        return HttpResponseRedirect('/')
    except Exception as e:
        return HttpResponse('Something went wrong in logging out...!' + '\n' + str(e))
