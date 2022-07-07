
from django.urls import path
from .views import *

app_name = "main"
urlpatterns = [
    path('', showmain, name="showmain"),
    path('intro/', intro, name='intro'),
    path('new/', new, name='new'),
    path('create/', create, name='create'),
    path('<str:id>', detail, name='detail'),
    path('/', SearchFormView.as_view(), name='search'),
    path('<str:id>/likes/', likes, name='likes'),
    
    path('community/', community, name='community'),
    path('community/<str:id>/', community_detail, name='community_detail'),
    path('community_new/', community_new, name='community_new'),
    path('community_create/', community_create, name='community_create'),

    path('<str:id>/comment_create', comment_create, name="comment_create"),
    path('<str:id>/comment_delete', comment_delete, name="comment_delete"),
    path('<str:id>/comment_edit', comment_edit, name="comment_edit"),
    path('<str:id>/comment_update', comment_update, name="comment_update"),
]