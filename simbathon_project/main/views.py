from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment, Community
from django.utils import timezone

# Create your views here.

def intro(request):
    return render(request, 'main/intro.html')

def showmain(request):
    posts = Post.objects.all()
    return render(request, 'main/mainpage.html', {'posts':posts})

def new(request):
    return render(request, 'main/posting.html')

def create(request):
    new_post = Post()
    new_post.title = request.POST['title']
    new_post.writer = request.user
    new_post.pub_date = timezone.now()
    new_post.category = request.POST['category']
    new_post.body = request.POST['body']
    new_post.image = request.FILES.get('image')
    new_post.save()
    return redirect('main:detail', new_post.id)

def detail(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'main/detail.html', {'post':post})

def community(request):
    communities = Community.objects.all()
    return render(request, 'main/community.html', {'communities':communities})

def community_detail(request, id):
    community = get_object_or_404(Community, pk=id)
    return render(request, 'main/community_detail.html', {'community':community})