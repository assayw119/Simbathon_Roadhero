
from django.urls import path
from .views import *

app_name = "main"
urlpatterns = [
    path('', showmain, name="showmain"),
    path('intro/', intro, name='intro'),
    path('new/', new, name='new'),
    path('create/', create, name='create'),
    path('<str:id>', detail, name='detail'),
    path('search/', SearchFormView.as_view(), name='search'),
    
    path('community/', community, name='community'),
    path('community/<str:id>/', community_detail, name='community_detail'),
    path('community_new/', community_new, name='community_new'),
    path('community_create/', community_create, name='community_create'),
]