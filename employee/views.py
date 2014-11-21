from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def index(request):
    if request.user.groups.filter(name='admin').exists():
        return HttpResponseRedirect('../hradmin/')
    else:
        return render(request, 'employee/index.html')
