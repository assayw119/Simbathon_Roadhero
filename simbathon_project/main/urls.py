
from django.urls import path
from .views import *

app_name = "main"
urlpatterns = [
    path('', showmain, name="showmain"),
    path('intro/', intro, name='intro'),
    path('new/', new, name='new'),
    path('create/', create, name='create'),
    path('<str:id>', detail, name='detail'),
    path('media/', SearchFormView.as_view(), name='search'),
    path('<str:id>/likes/', likes, name='likes'),

    path('community/', community, name='community'),
    path('community/<str:id>/', community_detail, name='community_detail'),
    path('community_new/', community_new, name='community_new'),
    path('community_create/', community_create, name='community_create'),
    path('community_update/', community_update, name='community_update'),
    path('<str:id>/community_delete', community_delete, name='community_delete'),

    path('<str:id>/comment_create', comment_create, name="comment_create"),
    path('<str:id>/comment_delete', comment_delete, name="comment_delete"),
    path('<str:id>/comment_edit', comment_edit, name="comment_edit"),
    path('<str:id>/comment_update', comment_update, name="comment_update"),

    path('<str:id>/community_comment_create', community_comment_create, name="community_comment_create"),
    path('<str:id>/community_comment_edit', community_comment_edit, name="community_comment_edit"),
    path('<str:id>/community_comment_update', community_comment_update, name="community_comment_update"),
    path('<str:id>/community_comment_delete', community_comment_delete, name="community_comment_delete"),
]
