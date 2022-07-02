
from django.urls import path
from .views import *

app_name = "main"
urlpatterns = [
    path('', showmain, name="showmain"),
    path('intro/', intro, name='intro'),
    path('new/', new, name='new'),
    path('create/', create, name='create'),
    path('<str:id>', detail, name='detail'),
]