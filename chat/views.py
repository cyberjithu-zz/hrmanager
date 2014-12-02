from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required(login_url='/')
def index(request):
    print '>>>>>>>', User.objects.all()[0].is_authenticated()
    return render(request, 'chat/index.html')
