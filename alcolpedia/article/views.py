from django.shortcuts import render,get_object_or_404,redirect
from article.models import *
from django.utils import timezone
from django.utils.timezone import localdate
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta


#술게임페이지
def table_contents(request):
    name= request.GET.get('name')
    try:
        contents_list = Content.objects.filter(sort = name)
        page_cnt = request.GET.get('page_cnt')
        if not page_cnt:
            page_cnt = 10
        paginator = Paginator(contents_list,page_cnt)
        page = request.GET.get('page')
        posts = paginator.get_page(page)
        if page == "" or page == None: 
            page = 1
        start = max(int(page)-5, 1)
        end = min(int(page)+5, paginator.num_pages)
        return render(request,name+'.html',{'posts' : posts,'range' : [i for i in range(start, end+1)]})
    except:
        return redirect('/')
#좋아요
@login_required
def like(request, content_id):
    content = get_object_or_404(Content,pk=content_id)
    content.like.add(request.user)
    content.save()    
    name = content.sort
    return redirect('/article/?name='+str(name))

#좋아요 취소
@login_required
def cancel(request, content_id):
    content = get_object_or_404(Content,pk=content_id)
    content.like.remove(request.user)
    content.save()    
    name = content.sort
    return redirect('/article/?name='+str(name))

#태그 누르면 검색됨
def tag(request,tag_id) : 
    tag = get_object_or_404(Tag,pk=tag_id)
    contents = Content.objects.filter(tag__id = tag.id)
    return render(request,'search.html',{'contents':contents})
 
#게시물 보기
def detail(request,content_id) :
    content = get_object_or_404(Content,pk = content_id)
    return render(request,'detail.html',{'content':content})

def filter(request) : 
    #변수받기
    var = request.GET.get('var')
    #변수=난이도
    if var in ('1','2','3') :
        list_contents = Content.objects.filter(difficulty = var)
    #변수=날짜
    elif var in ('7','30','90')  :
        time_threshold = datetime.now() - timedelta(days=int(var))
        print(time_threshold,datetime.now())
        list_contents = Content.objects.filter( dated_at__gt=time_threshold)
    #변수=태그
    else : 
        list_contents = Content.objects.filter(tag__title = var)
    return render(request,'game.html',{'posts' : list_contents})
