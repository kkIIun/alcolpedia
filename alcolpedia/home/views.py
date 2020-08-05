from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from django.utils import timezone
from django.utils.timezone import localdate
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

def List(request):
    contents = Content.objects.all()
    return render(request,'list.html',{'contents':contents})

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
