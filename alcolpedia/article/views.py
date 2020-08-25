from django.shortcuts import render,get_object_or_404,redirect
from article.models import *
from member.models import Profile
from django.utils import timezone
from django.utils.timezone import localdate
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from django.db.models import Q
from django.http import HttpResponse
import json


#술게임페이지
def table_contents(request):
    board_name = {'game': '술게임', 'bgm':'브금', 'alcohol': '폭탄주', 'cheers':'건배사', 'setting': '옵션'}
    name= request.GET.get('name')
    tag = Tag.objects.all()[:6]
    all_tags = Tag.objects.all()[6:]
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
    if request.user.is_authenticated :
        profile = get_object_or_404(Profile,user__username = request.user.username)
        return render(request,name+'.html',{'title': board_name[name],'posts' : posts,'range' : [i for i in range(start, end+1)],'profile':profile,'tags':tag,'all_tags':all_tags})
    else :
        return render(request,name+'.html',{'title': board_name[name], 'posts' : posts,'range' : [i for i in range(start, end+1)],'tags':tag,'all_tags':all_tags})
#좋아요
@login_required(login_url='/member/signin/')
def like(request):
    # ajax 통신을 통해서 template에서 POST방식으로 전달
    content_id = request.POST.get('content_id', None)

    content = get_object_or_404(Content, pk=content_id)

    if request.user in content.like.all():
        content.like.remove(request.user)
        isLiked = False
        message = "좋아요 취소"
    else:
        isLiked = True
        content.like.add(request.user)
        message = "좋아요"
    
    represent_user = ""
    if len(content.like.all()) > 0:
        represent_user = content.like.all()[0].username
    
    context = {'like_count': str(content.like_count()),
            'message': message,
            'username': str(request.user.username),
            "represent_user":represent_user,
            "isLiked": isLiked}
    
    return HttpResponse(json.dumps(context), content_type="application/json")

#태그 누르면 검색됨
def tag(request,tag_id) : 
    tag = get_object_or_404(Tag,pk=tag_id)
    contents = Content.objects.filter(tag__id = tag.id)
    try:
        profile = get_object_or_404(Profile, user__username = request.user.username)
        return render(request,'search.html',{'contents':contents,'profile':profile})
    except:
        return render(request,'search.html',{'contents':contents})
 
#게시물 보기
def detail(request,content_id) :
    content = get_object_or_404(Content,pk = content_id)
    if request.user.is_authenticated :
        profile = get_object_or_404(Profile,user__username = request.user.username)
        return render(request,'detail.html',{'title': content.title ,'content':content,'profile':profile})
    else :
        return render(request,'detail.html',{'title': content.title ,'content':content})

def filter(request) : 
    tags = Tag.objects.all()[:6]
    all_tags = Tag.objects.all()[6:]
    #변수받기
    difficulty = request.GET.get('difficulty')
    tag = request.GET.get('tag')
    date = request.GET.get('date')
    q = Q()
    if not difficulty or difficulty == '0' :
        difficulty = 0
    else :
        q.add(Q(difficulty = difficulty), q.AND)
    if not tag or tag == '0' :
        tag = 0
    else :
        q.add(Q(tag__title = tag), q.AND)
    if not date or date == '0' :
        date = 0
    else :
        time_threshold = datetime.now() - timedelta(days=int(date))
        q.add(Q(updated_at__gt = time_threshold), q.AND)
    list_contents = Content.objects.filter(q)
    print(difficulty,tag,date,type(difficulty),type(tag),type(date))
    if request.user.is_authenticated :
        profile = get_object_or_404(Profile,user__username = request.user.username)
        return render(request,'game.html',{'posts' : list_contents,'profile':profile,'tag':tag,'date':date,'difficulty':difficulty,'tags':tags,'all_tags':all_tags})
    else :
        return render(request,'game.html',{'posts' : list_contents,'tag':tag,'date':date,'difficulty':difficulty,'tags':tags,'all_tags':all_tags})
        
@login_required
def bookmark(request):

    content_id = request.POST.get('content_id', None)

    content = get_object_or_404(Content, pk=content_id)
    if request.user in content.bookmark.all():
        content.bookmark.remove(request.user)
        isBookmarked = False
        message = "북마크 취소"

    else:
        isBookmarked = True
        content.bookmark.add(request.user)
        message = "북마크"
    
    context = {
            'message': message,
            'username': str(request.user.username),
            "isBookmarked": isBookmarked}
    
    return HttpResponse(json.dumps(context), content_type="application/json")


    