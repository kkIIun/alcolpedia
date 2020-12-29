from django.shortcuts import render,get_object_or_404,redirect
from article.models import *
from member.models import Profile
from django.utils import timezone
from django.utils.timezone import localdate
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from django.db.models import Q
from functools import reduce
from operator import and_, or_
from django.http import HttpResponse
import json


def table_contents(request):
    board_name = {'game': '술게임', 'bgm':'브금', 'alcohol': '폭탄주', 'cheers':'건배사', 'setting': '옵션'}
    name= request.GET.get('name')
    tag = Tag.objects.all()[:6]
    all_tags = Tag.objects.all()[6:]
    contents_list = Content.objects.filter(sort = name).exclude(or_(Q(status = 'd'),Q(status = 'w')))
    page_cnt = request.GET.get('page_cnt')
    if not page_cnt:
        page_cnt = 6
    paginator = Paginator(contents_list,page_cnt)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    if page == "" or page == None: 
        page = 1
    start = max(int(page)-5, 1)
    end = min(int(page)+5, paginator.num_pages)
        


    for i in range(len(posts)):
        posts[i].no_blank_title = posts[i].title.replace(" ","")
        posts[i].no_blank_title = posts[i].no_blank_title.replace("!","")

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

    q = Q()

    content = get_object_or_404(Content,pk = content_id)
    tags = content.tag.all()
    for tag in tags:
        q.add(Q(tag__id = tag.id), q.OR)
    recommend_contents = Content.objects.filter(q)
    if request.user.is_authenticated :
        profile = get_object_or_404(Profile,user__username = request.user.username)
        return render(request,'detail.html',{'title': content.title ,'content':content,'profile':profile, 'tags': tags, 'recommend_contents' : recommend_contents })
    else :
        return render(request,'detail.html',{'title': content.title ,'content':content, 'tags': tags, 'recommend_contents' : recommend_contents})


def filter(request) : 
    tags = Tag.objects.all()[:6]
    all_tags = Tag.objects.all()[6:]
    #변수받기
    name = "game"
    try:
        name = request.GET.get('name')
    except:
        name = "game"

    try:
        difficulty = request.GET.get('difficulty')
        difficulty = int(difficulty)
        if difficulty == 0:
            difficulty_list = [0,1,2,3]
        else:
            difficulty_list = [difficulty]
    except:
        difficulty = 0
        difficulty_list= [0,1,2,3]

    try:
        tag = request.GET.getlist('tag')
        tag_list = tag
    except:
        tag_list = list(tags) + list(all_tags)
    else:
        if not tag or "".join(tag) == "":
            tag_list = list(tags) + list(all_tags)

    try:
        date = request.GET.get('date')
        time_threshold = (datetime.now() - timedelta(days=int(date)))
    except:
        time_threshold = datetime.now()- timedelta(days=100)
        date = None

    q = Q()


    q.add(Q(difficulty__in= difficulty_list)&Q(tag__title__in= tag_list)&Q(updated_at__gt=time_threshold), q.AND)
    q.add(Q(sort=name),q.AND)
    list_contents = Content.objects.filter(q)

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

def commenting(request, content_id):
    new_comment = Comment()
    new_comment.content = get_object_or_404(Content, pk=content_id)
    new_comment.author = request.user
    new_comment.body = request.POST.get('body')
    new_comment.save()
    return redirect('/article/?name=alcohol')
    
