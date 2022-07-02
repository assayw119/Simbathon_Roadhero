from django.shortcuts import render

from django.contrib.auth.models import User

# Create your views here.
def mypage(request):
    user = request.user
    return render(request, 'users/mypage.html', {})