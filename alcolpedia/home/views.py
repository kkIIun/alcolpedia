from django.shortcuts import render,get_object_or_404,redirect
from article.models import *
from member.models import Profile
from django.utils import timezone
from django.utils.timezone import localdate
from django.core.paginator import Paginator

#메인화면
def home(request):
    try:
        profile = get_object_or_404(Profile, user__username = request.user.username)
        return render(request, 'home.html',{'profile':profile})
    except :
        return render(request,'home.html')

#검색기능
def search(request) :
    q = request.GET.get('q')
    contents = Content.objects.filter(title__icontains=q)
    return render(request,'search.html',{'contents':contents})
# def detail(request, content_id):

