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


# from django.contrib.auth.models import User


@login_required(login_url='/')
def index(request):
    # context = {}
    # context['employees'] = EmployeeInfo.objects.exclude(user=request.user)
    # context['admins'] = HrAdminInfo.objects.exclude(user=request.user)
    # if request.user.groups.filter(name='admin').exists():
    #     context['user_data'] = HrAdminInfo.objects.filter(user=request.user)[0]
    # else:
    #     context['user_data'] = EmployeeInfo.objects.filter(user=request.user)[0]
    return HttpResponseRedirect('user-hradmin')
    # return render(request, 'chat/index.html', context)


def chatselect(request, username):
    print '>>>>>>>', username, request.user
    context = {}
    context['employees'] = EmployeeInfo.objects.exclude(user=request.user)
    context['admins'] = HrAdminInfo.objects.exclude(user=request.user)
    if request.user.groups.filter(name='admin').exists():
        context['user_data'] = HrAdminInfo.objects.filter(user=request.user)[0]
    else:
        context['user_data'] = EmployeeInfo.objects.filter(user=request.user)[0]
    user1 = User.objects.filter(username=username)[0]
    context['messages'] = Message.objects.filter(Q(sender=user1, receiver=request.user) | Q(sender=request.user, receiver=user1)).order_by('date_send')
    context['selected_user'] = username
    return render(request, 'chat/index.html', context)


def loadmessages(request):
    print request.body
    data = {'messages': ''}
    messages = []
    if request.method == "POST":
        data = json.loads(request.body)
        try:
            user1 = User.objects.filter(username=data['user1'])[0]
            user2 = User.objects.filter(username=data['user2'])[0]
            messages_objects = Message.objects.filter(Q(sender=user1, receiver=user2) | Q(sender=user2, receiver=user1)).order_by('date_send')
            for msg in messages_objects:
                message = model_to_dict(msg)
                message['sender'] = msg.sender.username
                message['receiver'] = msg.receiver.username
                messages.append(message)
            data = {'messages': messages}
        except:
            data = {'messages': ''}
    print data
    return HttpResponse(json.dumps(data,
                        cls=DjangoJSONEncoder), content_type="application/json")

