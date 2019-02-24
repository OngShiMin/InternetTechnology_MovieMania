from django.contrib import admin
from moviemania.models import UserProfile


# Register your models here.

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')


admin.site.register(UserProfile)
