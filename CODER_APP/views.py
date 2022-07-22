from django.shortcuts import render
from django.template import Context, Template

from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'templates/index.html')
