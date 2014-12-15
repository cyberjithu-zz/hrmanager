from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from employee.models import EmployeeInfo
from hradmin.models import HrAdminInfo
from chat.models import Message
from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from django.db.models import Q
import json
from django.core.serializers.json import DjangoJSONEncoder


@login_required(login_url='/')
def index(request):
    return HttpResponseRedirect('user-hradmin')


def chatselect(request, username):
    context = {}
    context['employees'] = EmployeeInfo.objects.exclude(user=request.user)
    context['admins'] = HrAdminInfo.objects.exclude(user=request.user)
    if request.user.groups.filter(name='admin').exists():
        context['user_data'] = HrAdminInfo.objects.get(user=request.user)
    else:
        context['user_data'] = EmployeeInfo.objects.get(user=request.user)
    user1 = User.objects.get(username=username)
    context['messages'] = Message.objects.filter(Q(sender=user1, receiver=request.user) | Q(sender=request.user, receiver=user1)).order_by('datetime')
    context['selected_user'] = username
    print '>>>>>>>>', context['messages']
    return render(request, 'chat/index.html', context)
