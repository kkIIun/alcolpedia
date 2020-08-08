from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from django.utils import timezone
from django.utils.timezone import localdate
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

def list_game(request):
    contents = Content.objects.filter(sort = 'game')
    print(contents)
    return render(request,'game.html',{'contents':contents})

def list_alcohol(request):
    contents = Content.objects.filter(sort = 'alcohol')
    return render(request,'alcohol.html',{'contents':contents})

def list_setting(request):
    contents = Content.objects.filter(sort = 'setting')
    return render(request,'setting.html',{'contents':contents})

def list_cheers(request):
    contents = Content.objects.filter(sort = 'cheers')
    return render(request,'cheers.html',{'contents':contents})

def list_bgm(request):
    contents = Content.objects.filter(sort = 'bgm')
    return render(request,'bgm.html',{'contents':contents})

@login_required
def like(request, content_id):
    content = get_object_or_404(Content,pk=content_id)
    content.like.add(request.user)
    content.save()    
    return redirect('List')

@login_required
def cancel(request, content_id):
    content = get_object_or_404(Content,pk=content_id)
    content.like.remove(request.user)
    content.save()    
    return redirect('List')

def search(request) :
    q = request.GET.get('q')
    contents = Content.objects.filter(title__icontains=q)
    return render(request,'search.html',{'contents':contents})

def tag(request,tag_id) : 
    tag = get_object_or_404(Tag,pk=tag_id)
    contents = Content.objects.filter(tag__id = tag.id)
    return render(request,'search.html',{'contents':contents})
# def detail(request, content_id):
