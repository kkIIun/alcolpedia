from django.shortcuts import redirect, render,get_object_or_404
from django.contrib.auth.models import User
from .models import Profile
from django.contrib import auth
from django.contrib import messages
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from .forms import SignInForm, SignUpForm

# 회원가입 기능
# POST 메서드로 `username`, `password`, `confirm_password`를 넘겨받아야 한다.
def sign_up(request):
    if request.method == "POST":
        if request.POST["password"] == "" or request.POST["password"] == None:
            messages.error(request,"비밀번호를 입력해주세요.")
            return render(request, 'sign_up.html', {"form": SignUpForm()})
        elif request.POST["password"]  != request.POST["confirm_password"]:
            messages.error(request, "비밀번호가 서로 다릅니다.")
            return render(request, 'sign_up.html', {"form": SignUpForm()}) 
        elif len(request.POST["password"]) < 4:
            messages.error(request, "비밀번호가 너무 짧습니다.")
            return render(request, 'sign_up.html', {"form": SignUpForm()}) 
        elif request.POST["password"]  == request.POST["confirm_password"]:
            try:
                user = User.objects.create_user(
                        username = request.POST["username"], 
                        password = request.POST["password"],
                    )
                auth.login(request, user)
                return redirect('home')
            except:
                messages.error(request, "다른 사용자가 사용중인 username입니다.")
                return render(request, 'sign_up.html', {"form": SignUpForm()}) 
    return render(request, 'sign_up.html', {"form": SignUpForm()})


# 로그인 기능
# POST 메서드로 'username', 'password'를 넘겨받아야 한다.
def sign_in(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username = username, password = password)

        if user:
            auth.login(request, user)
            return redirect('home')
        else:
            try:
                user = request.user
                auth.login(request, user)
                return redirect('home')
            except:
                messages.error(request, "username 혹은 password가 올바르지 않습니다.")
                return render(request, 'sign_in.html',  {"form": SignInForm()})

    return render(request, 'sign_in.html',  {"form": SignInForm()})

# 로그아웃 기능
def sign_out(request):
    auth.logout(request)
    return redirect('/')


@login_required
def profile(request):
    profile = get_object_or_404(Profile,user__username = request.user.username)
    user = get_object_or_404(User, pk = request.user.id)
    if request.method == 'POST' :
        name = request.POST.get('name')
        image = request.FILES.get('image')
        if name:
            user.username = name
        if image:
            profile.avatar = image
        user.save()
        profile.save()
        return render(request,'profile.html',{'profile':profile})
    else:
        return render(request,'profile.html',{'profile':profile})
