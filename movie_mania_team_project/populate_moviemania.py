import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'movie_mania_team_project.settings')

import django

django.setup()
from moviemania.models import Category, Movie


def populate():
    action_movies = [
        {"title": "Mission Impossible", "views": 32, "likes": 16, "content": "A classic action movie", "director":"Jack",
         "actor":"Lily", "img": "posters/MissionImpossibleFallout.jpg",
         "netflix_link": "", "amazon_link": "", "preview": "",
         },
        {"title": "Avengers: Infinity War", "views": 16, "likes": 32, "director":"Anthony Russo, Joe Russo",
         "actor":"Robert Downey Jr., Chris Hemsworth, Mark Ruffalo, Chris Evans, Scarlett Johansson, Don Cheadle, Benedict Cumberbatch,Tom Holland",
         "content": "The Avengers and their allies must be willing to sacrifice all in an attempt to defeat the powerful Thanos before his blitz of devastation and ruin puts an end to the universe.",
         "netflix_link": "", "amazon_link": "https://www.amazon.co.uk/dp/B07CLZKY26?ref_=imdbref_tt_wbr_aiv&tag=imdbtag_tt_wbr_aiv-21", "preview": "https://www.youtube.com/watch?v=6ZfuNTqbHE8","img": "posters/InfinityWar.jpg"
         },
         {"title": "Aquaman", "views": 32, "likes": 16, "content": "Arthur Curry, the human-born heir to the underwater kingdom of Atlantis, goes on a quest to prevent a war between the worlds of ocean and land.", 
         "director":"James Wan", "actor":"Jason Momoa, Amber Heard, Willem Dafoe", "img": "posters/AquaMan.jpg",
         "netflix_link": "", "amazon_link": "", "preview": "",
         },
    ]

    drama_movies = [
        {"title": "Bohemian Rhapsody", "views": 32, "likes": 16,
         "content": "The story of the legendary rock band Queen and lead singer Freddie Mercury, leading up to their famous performance at Live Aid (1985).",
         "netflix_link": "", "amazon_link": "", "preview": "https://www.youtube.com/watch?v=mP0VHJYFOAU",
         "director": "Bryan Singer", "actor": "Rami Malek, Lucy Boynton, Gwilym Lee", "img": "posters/BohemianRhapsody.jpg"},
        {"title": "Titanic", "views": 16, "likes": 16, "director": "Jack", "actor": "Lily",
         "content": "Tragic love story set on the Titanic",
         "netflix_link": "", "amazon_link": "https://www.amazon.co.uk/dp/B07JP1QM39?ref_=imdbref_tt_wbr_aiv&tag=imdbtag_tt_wbr_aiv-21", "preview": "", "img": "posters/Titanic.jpg"}
    ]

    fantasy_movies = [
        {"title": "Fantastic Beasts: The Crimes of Grindelwald", "views": 32, "likes": 16,
         "content": "In this sequel, the characters travel to Paris and meet Grindelwald",
         "netflix_link": "", "amazon_link": "", "preview": "",
         "director":"Jack","actor": "Lily", "img": "posters/CrimesOfGrindelwald.jpg"},
        {"title": "Fantastic Beasts and Where To Find Them", "likes": 15, "views": 10,
         "netflix_link": "https://www.netflix.com/title/80111501", "amazon_link": "",
         "preview": "https://www.youtube.com/watch?v=ViuDsy7yb8M", "director": "David Yates",
         "actor": "Eddie Redmayne, Katherine Waterston, Dan Fogler, Alison Sudol, Ezra Miller",
         "content": "Fantastic Beasts and Where to Find Them is a prequel to the Harry Potter movies. "
         "Based on J.K. Rowling's original story, it takes place in 1920s New York City and follows "
         "Newt Scamander (Eddie Redmayne), a magizoologist and author of a Hogwarts textbook.",
         "img": "posters/FantasticBeasts.jpg"}
        ]


    cats = {"Action": {"movies": action_movies},
            "Drama": {"movies": drama_movies},
            "Fantasy": {"movies": fantasy_movies}}

    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for m in cat_data["movies"]:
            add_movie(c, m["title"], m["views"], m["likes"], m["content"], m["director"], m["actor"], m["netflix_link"],
                      m["amazon_link"], m["img"], m["preview"] )

    for c in Category.objects.all():
        for p in Movie.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(m)))


def add_movie(cat, title, views, likes, content, director, actor, netflix_link, amazon_link, img, preview):
    m = Movie.objects.get_or_create(category=cat, title=title)[0]
    m.views = views
    m.likes = likes
    m.content = content
    m.director = director
    m.actor = actor
    m.netflix_link = netflix_link
    m.amazon_link = amazon_link
    m.preview = preview
    m.img = img

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
