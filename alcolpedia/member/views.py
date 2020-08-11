from django.shortcuts import redirect, render,get_object_or_404
from django.contrib.auth.models import User
from .models import Profile
from django.contrib import auth
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required

# 회원가입 기능
# POST 메서드로 `username`, `password`, `confirm_password`를 넘겨받아야 한다.
def sign_up(request):
    if request.method == "POST":
        # password, confirm_password가 정상적이 값인가?
        if request.POST["password"] and request.POST["confirm_password"]:
            print('pass1')
            # password와 confirn_password가 다른가?
            if(request.POST["password"] != request.POST["confirm_password"]):
                messages.error(request, "비밀번호가 서로 다릅니다.")
            
            else :
                try:
                    user = User.objects.create_user(
                        username = request.POST["username"], 
                        password = request.POST["password"],
                    )
                    user.create_user_profile()
                    auth.login(request,user)
                except:
                    messages.error(request, "다른 사용자가 사용 중인 username입니다.")
        else:
            messages.error(request, "비밀번호를 입력해주세요.")
        return redirect('home')
    else : 
        return render(request, 'sign_up.html')

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
                pass

    return render(request, 'sign_in.html')

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
        print(image)
        if name:
            user.username = name
        if image:
            profile.avatar = image
        user.save()
        profile.save()
        return redirect('home')
    else:
        return render(request,'profile.html',{'profile':profile})
