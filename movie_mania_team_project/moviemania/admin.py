from django.contrib import admin
from moviemania.models import UserProfile
from moviemania.models import Category, Movie


# Register your models here.

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Movie)
admin.site.register(UserProfile)
