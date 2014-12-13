from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from employee.models import EmployeeInfo


@login_required(login_url='/')
def index(request):
    context = {}
    if request.user.groups.filter(name='admin').exists():
        return HttpResponseRedirect('../hradmin/')
    else:
        context['user_data'] = EmployeeInfo.objects.get(user=request.user)
        return render(request, 'employee/index.html', context)
