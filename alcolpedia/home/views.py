from typing import ContextManager
from django.shortcuts import render,get_object_or_404,redirect
from article.models import *
from member.models import Profile
from django.utils.timezone import localdate
from django.core.paginator import Paginator
import urllib
from django.db.models import Q
from functools import reduce
from operator import and_, or_
from django.db.models import Count

#메인화면
def home(request):
    tag = Tag.objects.all()
    contents_list = Content.objects.annotate(like_count=Count('like')).filter(sort = "game", like_count__gt=-1).order_by('like_count','updated_at')
    contents_list_len = len(contents_list)
    contents_list = contents_list[:min(6,contents_list_len)]

    bgm_list = Content.objects.filter(sort = "bgm").order_by('updated_at')
    
    bgm_list_len = len(bgm_list)
    bgm_listt = bgm_list[:min(6,bgm_list_len)]

    try:
        profile = get_object_or_404(Profile, user__username = request.user.username)
        return render(request, 'home.html',{'title': 'Alcolpedia','profile':profile,'tags':tag, 'contents': contents_list, 'bgms': bgm_list})
    except :
        return render(request,'home.html',{'title': 'Alcolpedia','tags':tag, 'contents': contents_list, 'bgms': bgm_list})

#검색기능
def search(request) :
    search_words = request.GET.getlist('search_word')
    search_words = [urllib.parse.unquote(i) for i in search_words]

    tag_words = []
    query_words = []

    for i in search_words:
        if len(i) > 0:
            if i[0] == '#' and len(i) > 1:
                tag_words.append(i[1:])
            else:
                query_words.append(i)

    q = Q(tag__title__in= tag_words)
    for word in query_words:
        q |= Q(title__contains = word)

    contents = set(Content.objects.filter(q))
    try:
        profile = get_object_or_404(Profile, user__username = request.user.username)
        return render(request,'search.html',{'contents':contents,  'profile':profile, 'search_words' : search_words})
    except:
        return render(request,'search.html',{'contents':contents, 'search_words': search_words})

    return render(request,'search.html',{'search_words': search_words})
    # return render(request,'search.html')


def tag(request,tag_id) : 
    tag = get_object_or_404(Tag,pk=tag_id)
    contents = Content.objects.filter(tag__id = tag.id)
    try:
        profile = get_object_or_404(Profile, user__username = request.user.username)
        return render(request,'search.html',{'contents':contents,'profile':profile})
    except:
        return render(request,'search.html',{'contents':contents})
