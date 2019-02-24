from django.contrib import admin
from moviemania.models import UserProfile
from moviemania.models import Category, Movie


# Register your models here.

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')


admin.site.register(Category)
admin.site.register(Movie)
admin.site.register(UserProfile)
