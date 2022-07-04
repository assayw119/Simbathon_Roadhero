
from django.urls import path
from .views import *

app_name = "main"
urlpatterns = [
    path('', showmain, name="showmain"),
    path('intro/', intro, name='intro'),
    path('new/', new, name='new'),
    path('create/', create, name='create'),
    path('<str:id>', detail, name='detail'),
    path('community/', community, name='community'),
    path('<str:id>/', community_detail, name='community_detail'),
    path('community_new/', community_new, name='community_new'),
    path('community_create/', community_create, name='community_create'),
]