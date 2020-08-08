from django.shortcuts import render,get_object_or_404,redirect
from article.models import *
from django.utils import timezone
from django.utils.timezone import localdate
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

#술게임페이지
def game(request):
    contents = Content.objects.filter(sort = 'game')
    print(contents)
    return render(request,'game.html',{'contents':contents})

#폭탄주페이지
def alcohol(request):
    contents = Content.objects.filter(sort = 'alcohol')
    return render(request,'alcohol.html',{'contents':contents})

#옵션 페이지
def setting(request):
    contents = Content.objects.filter(sort = 'setting')
    return render(request,'setting.html',{'contents':contents})

#건배사 페이지
def cheers(request):
    contents = Content.objects.filter(sort = 'cheers')
    return render(request,'cheers.html',{'contents':contents})

#브금 페이지
def bgm(request):
    contents = Content.objects.filter(sort = 'bgm')
    return render(request,'bgm.html',{'contents':contents})

#좋아요
@login_required
def like(request, content_id):
    content = get_object_or_404(Content,pk=content_id)
    content.like.add(request.user)
    content.save()    
    return redirect('List')

#좋아요 취소
@login_required
def cancel(request, content_id):
    content = get_object_or_404(Content,pk=content_id)
    content.like.remove(request.user)
    content.save()    
    return redirect('List')

#태그 누르면 검색됨
def tag(request,tag_id) : 
    tag = get_object_or_404(Tag,pk=tag_id)
    contents = Content.objects.filter(tag__id = tag.id)
    return render(request,'search.html',{'contents':contents})
