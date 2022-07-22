from django.shortcuts import render
from django.template import Context, Template

from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'templates/CODER_APP/index.html')

def schedule(request):
    return render(request,'templates/CODER_APP/schedule.html')

def standings(request):
    return render(request,'templates/CODER_APP/standings.html')

def drivers(request):
    return render(request,'templates/CODER_APP/standings.html')

def news(request):
    return render(request,'templates/CODER_APP/news.html')

def facebook(request):
    return render(request,'templates/CODER_APP/facebook.html')

def twitter(request):
    return render(request,'templates/CODER_APP/twiiter.html')

def instagram(request):
    return render(request, 'templates/CODER_APP/instagram.html')

def about(request):
    return render(request, 'templates/CODER_APP/about.html')

def contact(request):
    return render(request, 'templates/CODER_APP/contact.html')

def terms(request):
    return render(request, 'templates/CODER_APP/terms.html')

def policy(request):
    return render(request, 'templates/CODER_APP/policy.html')

