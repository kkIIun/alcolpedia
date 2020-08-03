from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from django.utils import timezone
from django.utils.timezone import localdate
from django.core.paginator import Paginator

def home(request):
    return render(request, 'home.html')

def List(request):
    contents = Content.objects.all()
    return render(request,'list.html',{'contents':contents})