from django.urls import path
from .views import *

app_name = 'accounts'
urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('mypage/', mypage, name='mypage'),
    path('createinfo/', createInfo, name='createinfo'),
    path('editinfo/', editInfo, name='editinfo'),
    path('updateinfo/', updateInfo, name='updateinfo'),
]