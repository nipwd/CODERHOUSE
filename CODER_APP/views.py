from django.shortcuts import render
from django.template import Context, Template
from CODER_APP.models import *
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'templates/index.html')

def schedule(request):
    return render(request,'templates/CODER_APP/schedule/schedule.html')

def standings(request):
    return render(request,'templates/CODER_APP/standings/standings.html')

def drivers(request):
    return render(request,'templates/CODER_APP/drivers/drivers.html')

def teams(request):
    return render(request,'templates/CODER_APP/teams/teams.html')

