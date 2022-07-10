from tkinter.messagebox import NO
from unicodedata import category
from django.shortcuts import render, redirect, get_object_or_404

from main.forms import PostSearchForm, CommunitySearchForm
from .models import Post, Comment, Community, CommunityComment
from django.utils import timezone
from django.db.models import Q
from django.views.generic import FormView

# 인트로 페이지


def intro(request):
    return render(request, 'main/intro.html')

# 메인 페이지 (매거진 페이지)


def showmain(request):

    if request.method == 'GET':
        magazine_sort = request.GET.get('magazine')
        if magazine_sort == 'all' or magazine_sort == None:
            posts = Post.objects.all().order_by('-view_users')
        else:
            posts = Post.objects.filter(category=magazine_sort).order_by('-view_users')
    managers = ['roadhero']
    context = {'posts':posts, 'managers':managers}
    return render(request, 'main/mainpage.html', context)


class SearchFormView(FormView):
    template_name = 'main/mainpage.html'
    form_class = PostSearchForm

    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']
        posts = Post.objects.filter(
            Q(title__icontains=searchWord) | Q(body__icontains=searchWord))

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
    # print(post.view_users)
    post.view_users = int(post.view_users)+1
    # print(post.view_users)
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
    # 댓글을 최신순으로 정렬하는 코드
    all_comments = post.comments.all().order_by('-created_at')
    return render(request, 'main/detail.html', {'post': post, 'comments': all_comments})

# detail 수정 삭제(박영신)


def detail_edit(request, id):
    edit_post = Post.objects.get(id=id)
    return render(request, 'main/detail_edit.html', {'post': edit_post})


def detail_update(request, id):
    update_post = Post.objects.get(id=id)
    update_post.title = request.POST['title']
    update_post.writer = request.user
    update_post.pub_date = timezone.now()
    update_post.body = request.POST['body']
    if request.FILES.get("image"):
        update_post.image = request.FILES.get("image")
    update_post.save()
    return redirect('main:detail', update_post.id)


def detail_delete(request, id):
    delete_post = Post.objects.get(id=id)
    if request.user == delete_post.writer:
        delete_post.delete()
    return redirect('main:showmain')

# 커뮤니티 페이지


def community(request):
    
    context = {}
    communities = Community.objects.all().order_by('-view_users')
    if communities:
        context['first'] = communities[0]
    if request.method == 'GET':
        community_sort = request.GET.get('community')
        if community_sort == 'all' or community_sort == None:
            pass
        else:
            communities = Community.objects.filter(category=community_sort).order_by('-view_users')
        
    context['communities'] = communities
    print(context)
    return render(request, 'main/community.html', context)



class CommunitySearchFormView(FormView):
    template_name = 'main/community.html'
    form_class = CommunitySearchForm

    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']
        print(searchWord)
        communities = Community.objects.filter(
            Q(title__icontains=searchWord) | Q(body__icontains=searchWord))
        print(communities)
        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['communities'] = communities

        return render(self.request, self.template_name, context)


def community_detail(request, id):
    community = get_object_or_404(Community, pk=id)
    community.view_users = int(community.view_users)+1
    community.save()

    contents = community.communitycomments.all().order_by('-created_at')
    return render(request, 'main/community_detail.html', {'community': community, 'communitycomments': contents})


def community_new(request):
    return render(request, 'main/writing.html')


def community_create(request):
    new_community = Community()
    new_community.title = request.POST['title']
    new_community.writer = request.user
    new_community.pub_date = timezone.now()
    new_community.category = request.POST['category']
    new_community.body = request.POST['body']
    new_community.image = request.FILES.get('image')
    new_community.save()
    return redirect('main:community_detail', new_community.id)

# community 게시글 수정 기능 수정(삭제는 이미 구현 완료되어 있었네요!)


def community_update(request, id):
    update_community = Community.objects.get(id=id)
    update_community.title = request.POST['title']
    update_community.writer = request.user
    update_community.pub_date = timezone.now()
    update_community.body = request.POST['body']
    if request.FILES.get("image"):
        update_community.image = request.FILES.get("image")
    update_community.save()
    return redirect('main:community_detail', update_community.id)


def community_edit(request, id):
    edit_community = Community.objects.get(id=id)
    return render(request, 'main/community_edit.html', {'community': edit_community})


def community_delete(request, id):
    delete_community = Community.objects.get(id=id)
    if request.user == delete_community.writer:
        delete_community.delete()
    return redirect("main:community")


def community_likes(request, id):
    if request.user.is_authenticated:
        community = get_object_or_404(Community, pk=id)

        if community.like_users.filter(pk=request.user.pk).exists():
            # print(request.user.pk)
            # print(community.like_users.filter(pk=request.user.pk))
            community.like_users.remove(request.user)
        else:
            community.like_users.add(request.user)
        return redirect('main:community_detail', community.id)
    return redirect('accounts:login')


# detail 댓글 페이지

def comment_create(request, id):
    if request.method == "POST":
        post = get_object_or_404(Post, pk=id)
        current_user = request.user
        comment_content = request.POST.get("content")
        if len(comment_content.strip()) != 0:
            Comment.objects.create(content=comment_content,
                                   writer=current_user, post=post)
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

# 커뮤니티 댓글 페이지


def community_comment_create(request, id):
    if request.method == "POST":
        community = get_object_or_404(Community, pk=id)
        current_user = request.user
        community_comment_content = request.POST.get("comment")
        if len(community_comment_content.strip() == 0):
            CommunityComment.objects.create(
                content=community_comment_content, writer=current_user, community=community)
    return redirect("main:community_detail", id)


def community_comment_edit(request, id):
    communitycomment = CommunityComment.objects.get(id=id)
    if request.user == communitycomment.writer:
        return render(request, "main/community_comment_edit.html", {"communitycomment": communitycomment})
    else:
        return redirect("main:community_detail", communitycomment.community.id)


def community_comment_update(request, id):
    communitycomment = CommunityComment.objects.get(id=id)
    communitycomment.content = request.POST.get("comment")
    communitycomment.save()
    return redirect("main:community_detail", communitycomment.community.id)


def community_comment_delete(request, id):
    communitycomment = CommunityComment.objects.get(id=id)
    if request.user == communitycomment.writer:
        communitycomment.delete()
    return redirect("main:community_detail", communitycomment.community.id)


def about(request):
    return render(request, 'main/about.html')
