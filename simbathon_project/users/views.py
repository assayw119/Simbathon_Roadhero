# from django.shortcuts import render, redirect, get_object_or_404
# from main.models import Post
# from django.contrib.auth.models import User
# from .models import Profile
# from .forms import ProfileForm

# # Create your views here.
# def mypage(request):
#     # user = User.objects.get(pk=username)
#     # if user.profile:
#     #     profile = user.profile
#     #     return render(request, 'users/mypage.html', {'profile':profile})
#     # else:
#     #     return redirect('users:newinfo', user.pk)


#     user = request.user
#     # posts = Post.objects.filter(writer=user)
#     profile = Profile.objects.filter(user=user)
#     context = {
#         # 'posts':posts,
#         'profile':profile}
#     return render(request, 'users/mypage.html', context)

# def newInfo(request):
#     return render(request, 'users/newinfo.html')

# def createInfo(request):
#     if request.method == 'POST':
#         form = ProfileForm(request.POST)
#         if form.is_valid():
#             profile = form.save(commit=False)
#             profile.user = request.user
#             profile.save()
#             return redirect('users:mypage', profile)
#     else:
#         form = ProfileForm()
#     context = {'form':form}
#     return render(request, 'users:mypage', context)
#     # new_info = Profile()
#     # new_info.user = request.user
#     # new_info.name = request.POST['name']
#     # new_info.university = request.POST['university']
#     # new_info.major = request.POST['major']
#     # new_info.save()
#     # return redirect('users:mypage', new_info.user)
