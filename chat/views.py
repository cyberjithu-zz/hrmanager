from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required


@login_required(login_url='/')
def index(request):
    return render(request, 'chat/index.html')
