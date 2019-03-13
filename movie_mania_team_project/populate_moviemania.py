import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'movie_mania_team_project.settings')

import django

django.setup()
from moviemania.models import Category, Movie


def populate():
    action_movies = [
        {"title": "Mission Impossible", "views": 32,"director":"Jack","actor":"Lily"},
        {"title": "Avengers: Infinity War", "views": 16, "director":"Jack","actor":"Lily"}
    ]

    drama_movies = [
        {"title": "Bohemian Rhapsody", "views": 32, "director": "Jack", "actor": "Lily"},
        {"title": "Titanic", "views": 16, "director": "Jack", "actor": "Lily"}
    ]

    fantasy_movies = [
        {"title": "Fantastic Beasts: The Crimes of Grindelwald", "views": 32,"director":"Jack","actor":"Lily"}
    ]

    cats = {"Action": {"movies": action_movies},
            "Drama": {"movies": drama_movies},
            "Fantasy": {"movies": fantasy_movies}}

    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for m in cat_data["movies"]:
            add_movie(c, m["title"], m["views"])

    for c in Category.objects.all():
        for p in Movie.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(m)))


def add_movie(cat, title, views=0, ):
    m = Movie.objects.get_or_create(category=cat, title=title)[0]
    m.views = views
    m.save()
    return m


def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c


# Start execution here
if __name__ == '__main__':
    print("Starting MovieMania population script...")
    populate()
