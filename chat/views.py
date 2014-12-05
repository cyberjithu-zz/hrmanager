from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from employee.models import EmployeeInfo
from hradmin.models import HrAdminInfo
from django.forms.models import model_to_dict

# from django.contrib.auth.models import User


@login_required(login_url='/')
def index(request):
    context = {}
    context['employees'] = EmployeeInfo.objects.exclude(user=request.user)
    context['admins'] = HrAdminInfo.objects.exclude(user=request.user)
    if request.user.groups.filter(name='admin').exists():
        context['user_data'] = HrAdminInfo.objects.filter(user=request.user)[0]
    else:
        context['user_data'] = EmployeeInfo.objects.filter(user=request.user)[0]
    return render(request, 'chat/index.html', context)


def getmessages(request):
    print 'AAAAAAAAAa'
    return 'aaaaa'
    #return HttpResponse('Test message')
