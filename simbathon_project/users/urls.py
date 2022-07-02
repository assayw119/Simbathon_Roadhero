from django.urls import path
from .views import *

app_name = 'users'
urlpatterns = [
    path('mypage/', mypage, name='mypage'),
    path('newInfo/', newInfo, name='newinfo'),
    path('createInfo/', createInfo, name='createinfo'),
]