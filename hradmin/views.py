from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from employee.models import EmployeeInfo
from hradmin.models import HrAdminInfo
from django.forms.models import model_to_dict
# Create your views here.


@login_required(login_url='/')
def index(request):
    context = {}
    if request.user.groups.filter(name='admin').exists():
        context['user_data'] = HrAdminInfo.objects.filter(user=request.user)[0]
        context['employees'] = EmployeeInfo.objects.all()
        return render(request, 'hradmin/index.html', context)
    else:
        return HttpResponseRedirect('../employee/')
