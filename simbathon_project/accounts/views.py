from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth import get_user_model
from .models import Profile
from .forms import ProfileForm

# Create your views here.
# def login(request):
#     if request.method == 'POST':
#         pass
#     elif request.method == 'GET':
#         return render(request, 'login.html')

def login(request):
    # POST 요청 들어오면 로그인
    if request.method == 'POST':
        usr = request.POST['username']
        pwd = request.POST['password']
        # User 모델에 usr와 pwd가 일치하는 객체 있는지 확인
        # 있으면 해당 객체, 없으면 None 반환
        user = auth.authenticate(request, username=usr, password=pwd)

        if user is not None: # 유저가 존재할 경우
            auth.login(request, user)
            return redirect('main:showmain')
        else:
            # 만약 유저 없을경우 다시 로그인 화면으로
            return render(request, 'login.html')
    
    # GET 요청 들어오면 login form 담은 html 보여줌
    elif request.method == 'GET':
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('main:showmain')

def mypage(request):
    # person = get_object_or_404(get_user_model(), username=username)
    user = request.user
    # profile = Profile.objects.filter(user=str(username))
    # profile = get_object_or_404(Profile, user=username)
    profile = Profile.objects.get(user=user)
    return render(request, 'mypage.html', {'profile':profile})

def createInfo(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('accounts:mypage', profile)
    else:
        form = ProfileForm()
    context = {'form':form}
    return render(request, 'accounts:mypage', context)
    # new_info = Profile()
    # new_info.user = request.user
    # new_info.name = request.POST['name']
    # new_info.university = request.POST['university']
    # new_info.major = request.POST['major']
    # new_info.save()
    # return redirect('users:mypage', new_info.user)

def editInfo(request):
    user = request.user
    edit_profile = Profile.objects.get(user=user)
    return render(request, 'editinfo.html', {'profile':edit_profile})

def updateInfo(request):
    user = request.user
    update_profile = Profile.objects.get(user=user)
    update_profile.name = request.POST['name']
    update_profile.university = request.POST['university']
    update_profile.major = request.POST['major']
    update_profile.save()
    return redirect('accounts:mypage')