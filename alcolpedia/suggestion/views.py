from django.shortcuts import render,redirect
from .models import Suggetion
from django.utils import timezone

# Create your views here.
def create(request):
    suggetion = Suggetion()
    suggetion.title = request.POST.get('title')
    suggetion.body = request.POST.get('body')
    suggetion.date = timezone.datetime.now()
    suggetion.save()
    return redirect('/')