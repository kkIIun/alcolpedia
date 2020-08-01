from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from django.utils import timezone
from django.utils.timezone import localdate
from django.core.paginator import Paginator

def home(req):
    contents = Content.objects.all()
    return render(req,'home.html',{'contents':contents})
# Create your views here.
