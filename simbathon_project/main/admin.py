from django.contrib import admin
from .models import Post, Community, CommunityComment
# Register your models here.
admin.site.register(Post)
admin.site.register(Community)
admin.site.register(CommunityComment)