from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def index(request):
	return HttpResponse("Username is fuck")

def detail(request,uname):
    return HttpResponse("Username:-  %s.  " % uname)

def rating(request,uname):
    return HttpResponse("Rating %s." %uname)