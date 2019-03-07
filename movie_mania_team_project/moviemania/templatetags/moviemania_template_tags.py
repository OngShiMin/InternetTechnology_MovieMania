from django import template
from moviemania.models import Movie
from moviemania.models import Category

register = template.Library()


@register.inclusion_tag('moviemania/movies.html')
def get_movie_list():
    return {'movies': Movie.objects.all(),}

@register.inclusion_tag('moviemania/categories.html')
def get_category_list():
    return {'categories': Category.objects.all(),}



