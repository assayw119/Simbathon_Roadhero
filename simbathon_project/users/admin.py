# from django.contrib import admin
# from .models import Profile
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import User
# # Register your models here.

# class ProfileAdmin(admin.StackedInline):
#     model = Profile
#     con_delete = False

# class CustomUserAdmin(UserAdmin):
#     inlines = (ProfileAdmin,)

# admin.site.unregister(User)
# admin.site.register(User, CustomUserAdmin)