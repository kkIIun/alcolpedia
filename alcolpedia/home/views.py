from django.shortcuts import render,get_object_or_404,redirect
from article.models import *
from member.models import Profile
from django.utils.timezone import localdate
from django.core.paginator import Paginator

#메인화면
def home(request):
    tag = Tag.objects.all()
    try:
        profile = get_object_or_404(Profile, user__username = request.user.username)
        return render(request, 'home.html',{'profile':profile,'tags':tag})
    except :
        return render(request,'home.html',{'tags':tag})

#검색기능
def search(request) :
    q = request.GET.get('q')
    if q :
        contents = Content.objects.filter(title__icontains=q)
        return render(request,'search.html',{'contents':contents})
    else : 
        return render(request,'search.html')
# def detail(request, content_id):

