from django import template
from moviemania.models import Movie

register = template.Library()


@register.inclusion_tag('moviemania/movies.html')
def get_movie_list():
    return {'movies': Movie.objects.all(),}



