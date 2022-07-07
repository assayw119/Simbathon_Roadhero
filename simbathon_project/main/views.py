from tkinter.messagebox import NO
from unicodedata import category
from django.shortcuts import render, redirect, get_object_or_404

from main.forms import PostSearchForm
from .models import Post, Comment, Community
from django.utils import timezone
from django.db.models import Q
from django.views.generic import FormView

# 인트로 페이지


def intro(request):
    return render(request, 'main/intro.html')

# 메인 페이지 (매거진 페이지)


def showmain(request):
    
    if request.method=='GET':
        magazine_sort = request.GET.get('magazine')
        if magazine_sort == 'all' or magazine_sort == None:
            posts = Post.objects.all()
        else:
            posts = Post.objects.filter(category=magazine_sort)
    
    return render(request, 'main/mainpage.html', {'posts': posts})

class SearchFormView(FormView):
    template_name = 'main/mainpage.html'
    form_class = PostSearchForm
    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']
        posts = Post.objects.filter(Q(title__icontains=searchWord) | Q(body__icontains=searchWord))

        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['posts'] = posts

        return render(self.request, self.template_name, context)

def likes(request, id):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=id)

        if post.like_users.filter(pk=request.user.pk).exists():
            print(request.user.pk)
            print(post.like_users.filter(pk=request.user.pk))
            post.like_users.remove(request.user)
        else:
            post.like_users.add(request.user)
        return redirect('main:detail', post.id)
    return redirect('accounts:login')

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
    print(post.view_users)
    post.view_users = int(post.view_users)+1
    print(post.view_users)
    post.save()
    # session_cookie = request.user.id
    # cookie_name = f'post_viewer:{session_cookie}'
    # context = {
    #     'post':post,
    # }
    # response = render(request, 'main/detail.html', context)

    # if request.COOKIES.get(cookie_name) is not None:
    #     cookies = request.COOKIES.get(cookie_name)
    #     cookies_list = cookies.splot('|')
    #     if str(id) not in cookies_list:
    #         response.set_cookie(cookie_name, cookies + f'|{id}', expires=None)
    #         post.view_users += 1
    #         post.save()
    #         return response
        
    #     else:
    #         response.set_cookie(cookie_name, id, expires=None)
    #         post.view_users += 1
    #         post.save()
    #         return response
    #     return render(request, 'main/detail.html', context)
    ##댓글을 최신순으로 정렬하는 코드
    all_comments = post.comments.all().order_by('-created_at')
    return render(request, 'main/detail.html', {'post':post, 'comments':all_comments})

# 커뮤니티 페이지


def community(request):
    first_community = Community.objects.first()
    communities = Community.objects.all()
    return render(request, 'main/community.html', {'communities': communities, 'first': first_community})


def community_detail(request, id):
    community = get_object_or_404(Community, pk=id)
    return render(request, 'main/community_detail.html', {'community': community})


def community_new(request):
    return render(request, 'main/writing.html')


def community_create(request):
    new_community = Community()
    new_community.title = request.POST['title']
    new_community.writer = request.user
    new_community.pub_date = timezone.now()
    new_community.category = request.POST['category']
    new_community.body = request.POST['body']
    new_community.save()
    return redirect('main:community_detail', new_community.id)

## 댓글 페이지
def comment_create(request, id):
    if request.method == "POST":
        post = get_object_or_404(Post, pk=id)
        current_user = request.user
        comment_content = request.POST.get("content")
        Comment.objects.create(content=comment_content, writer=current_user, post=post)
    return redirect("main:detail", id)

def comment_edit(request, id):
    comment = Comment.objects.get(id=id)
    if request.user == comment.writer:
        return render(request, "main/comment_edit.html", {"comment": comment})
    else:
        return redirect("main:detail", comment.post.id)

def comment_delete(request, id):
    comment = Comment.objects.get(id=id)
    if request.user == comment.writer:
        comment.delete()
    return redirect("main:detail", comment.post.id)

def comment_update(request, id):
    comment = Comment.objects.get(id=id)
    comment.content = request.POST.get("content")
    comment.save()
    return redirect("main:detail", comment.post.id)