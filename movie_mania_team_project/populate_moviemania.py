import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'movie_mania_team_project.settings')

import django

django.setup()
from moviemania.models import Category, Movie


def populate():
    action_movies = [
        {"title": "Mission Impossible", "views": 20, "likes": 16, 
         "content": "Ethan Hunt and his IMF team, along with some familiar allies, race against time after a mission gone wrong.", 
         "director":"Christopher McQuarrie",
         "actor":"Tom Cruise, Henry Cavill, Ving Rhames ", 
         "img": "posters/MissionImpossibleFallout.jpg",
         "netflix_link": "", 
         "amazon_link": "https://www.amazon.co.uk/dp/B07FVT82JW?ref_=imdbref_tt_wbr_aiv&tag=imdbtag_tt_wbr_aiv-21", 
         "preview": "https://www.youtube.com/watch?v=wb49-oV0F78"},
         
        {"title": "The Fast and the Furious: Tokyo Drift", "views": 16, "likes": 32, 
         "director":"Justin Lin",
         "actor":"Lucas Black, Zachery Ty Bryan, Shad Moss",
         "content": "A teenager becomes a major competitor in the world of drift racing after moving in with his father in Tokyo to avoid a jail sentence in America.",
         "netflix_link": "", 
         "amazon_link": "https://www.amazon.co.uk/dp/B00FZQWZUM?ref_=imdbref_tt_wbr_aiv&tag=imdbtag_tt_wbr_aiv-21", 
         "preview": "https://www.youtube.com/watch?v=p8HQ2JLlc4E", 
         "img": "posters/Fast&Furious.jpg"},
         
        {"title": "Captain America: The First Avenger", "views": 32, "likes": 16, 
         "content": "Steve Rogers, a rejected military soldier transforms into Captain America after taking a dose of a 'Super-Soldier serum'." 
         "But being Captain America comes at a price as he attempts to take down a war monger and a terrorist organization.", 
         "director":"Joe Johnston", "actor":"Chris Evans, Hugo Weaving, Samuel L. Jackson", 
         "img": "posters/Captain1.jpg",
         "netflix_link": "", 
         "amazon_link": "https://www.amazon.co.uk/dp/B00O7KSORU?ref_=imdbref_tt_wbr_aiv&tag=imdbtag_tt_wbr_aiv-21", 
         "preview": "https://www.youtube.com/watch?v=JerVrbLldXw"},
    ]

    drama_movies = [
        {"title": "Bohemian Rhapsody", "views": 34, "likes": 26,
         "content": "The story of the legendary rock band Queen and lead singer Freddie Mercury, leading up to their famous performance at Live Aid (1985).",
         "netflix_link": "", 
         "amazon_link": "", 
         "preview": "https://www.youtube.com/watch?v=mP0VHJYFOAU",
         "director": "Bryan Singer", 
         "actor": "Rami Malek, Lucy Boynton, Gwilym Lee", 
         "img": "posters/BohemianRhapsody.jpg"},
         
        {"title": "Titanic", "views": 16, "likes": 16, 
         "director": "James Cameron", 
         "actor": "Leonardo DiCaprio, Kate Winslet",
         "content": "An American epic romance and disaster film, telling the story of the sinking of the RMS Titanic",
         "netflix_link": "", 
         "amazon_link": "https://www.amazon.co.uk/dp/B019HYDKBK?ref_=imdbref_tt_wbr_aiv&tag=imdbtag_tt_wbr_aiv-21",
         "preview": "", 
         "img": "posters/Titanic.jpg"},
         
        {"title": "12 Years a Slave", "views": 16, "likes": 8, 
         "director": "Steve McQueen", 
         "actor": " Chiwetel Ejiofor, Michael Kenneth Williams, Michael Fassbender",
         "content": "In the antebellum United States, Solomon Northup, a free black man from upstate New York, is abducted and sold into slavery.",
         "netflix_link": "", 
         "amazon_link": "https://www.amazon.co.uk/dp/B00J9G6320?ref_=imdbref_tt_wbr_aiv&tag=imdbtag_tt_wbr_aiv-21", 
         "preview": "https://www.youtube.com/watch?v=z02Ie8wKKRg", 
         "img": "posters/12YearsASlave.jpg"}
    ]

    fantasy_movies = [
        {"title": "Fantastic Beasts: The Crimes of Grindelwald", "views": 32, "likes": 23,
         "content": "In this sequel, the characters travel to Paris and meet Grindelwald",
         "netflix_link": "", 
         "amazon_link": "", "preview": "https://www.youtube.com/watch?v=vvFybpmyB9E",
         "director":"David Yates",
         "actor": "Eddie Redmayne, Katherine Waterston, Dan Fogler", 
         "img": "posters/CrimesOfGrindelwald.jpg"},
         
        {"title": "Fantastic Beasts and Where To Find Them", "likes": 15, "views": 18,
         "netflix_link": "", "amazon_link": "",
         "preview": "https://www.youtube.com/watch?v=ViuDsy7yb8M", 
         "director": "David Yates",
         "actor": "Eddie Redmayne, Katherine Waterston, Dan Fogler, Alison Sudol, Ezra Miller",
         "content": "Fantastic Beasts and Where to Find Them is a prequel to the Harry Potter movies. Based on J.K. Rowling's original story, it takes place in 1920s New York City and follows Newt Scamander (Eddie Redmayne), a magizoologist and author of a Hogwarts textbook.",
         "img": "posters/FantasticBeasts.jpg"},
         
        {"title": "Miss Peregrine's Home for Peculiar Children", "likes": 20, "views": 30,
         "netflix_link": "", 
         "amazon_link": "https://www.amazon.co.uk/dp/B01LXO031H?ref_=imdbref_tt_wbr_aiv&tag=imdbtag_tt_wbr_aiv-21",
         "preview": "https://www.youtube.com/watch?v=tV_IhWE4LP0", 
         "director": "Tim Burton",
         "actor": "E Eva Green, Asa Butterfield, Samuel L. Jackson ",
         "content": "When Jacob discovers clues to a mystery that stretches across time, he finds Miss Peregrine's Home for Peculiar Children. But the danger deepens after he gets to know the residents and learns about their special powers.",
         "img": "posters/MissPeregrine.jpg"},
         
         {"title": "Snow White and the Huntsman", "views": 16, "likes": 32, 
          "director":"Rupert Sanders",
         "actor":" Kristen Stewart, Chris Hemsworth, Charlize Theron",
         "content": "In a twist to the fairy tale, the Huntsman ordered to take Snow White into the woods to be killed winds up becoming her protector and mentor in a quest to vanquish the Evil Queen.",
         "netflix_link": "https://www.netflix.com/title/70217912", 
         "amazon_link": "https://www.amazon.co.uk/dp/B07CLZKY26?ref_=imdbref_tt_wbr_aiv&tag=imdbtag_tt_wbr_aiv-21", 
         "preview": "https://www.youtube.com/watch?v=-bT8UGtgzkE",
         "img": "posters/Snow.jpg"
         },
        ]
    
    
    scifi_movies = [
        {"title": "Thor: Ragnarok", "views": 32, "likes": 16,
         "content": "Thor is imprisoned on the planet Sakaar, and must race against time to return to Asgard and stop Ragnarök, the destruction of his world, at the hands of the powerful and ruthless villain Hela.",
         "netflix_link": "", 
         "amazon_link": "https://www.amazon.co.uk/dp/B076MJT3F6?ref_=imdbref_tt_wbr_aiv&tag=imdbtag_tt_wbr_aiv-21", 
         "preview": "https://www.youtube.com/watch?v=ue80QwXMRHg",
         "director":"Taika Waititi",
         "actor": " Chris Hemsworth, Tom Hiddleston, Cate Blanchett ", 
         "img": "posters/ThorRagnarok.jpg"},
         
        {"title": "Avengers: Infinity War", "views": 16, "likes": 32, 
         "director":"Anthony Russo, Joe Russo",
         "actor":"Robert Downey Jr., Chris Hemsworth, Mark Ruffalo, Chris Evans, Scarlett Johansson, Don Cheadle, Benedict Cumberbatch,Tom Holland",
         "content": "The Avengers and their allies must be willing to sacrifice all in an attempt to defeat the powerful Thanos before his blitz of devastation and ruin puts an end to the universe.",
         "netflix_link": "", 
         "amazon_link": "https://www.amazon.co.uk/dp/B07CLZKY26?ref_=imdbref_tt_wbr_aiv&tag=imdbtag_tt_wbr_aiv-21", 
         "preview": "https://www.youtube.com/watch?v=6ZfuNTqbHE8",
         "img": "posters/InfinityWar.jpg"},
          
        {"title": "Aquaman", "views": 32, "likes": 16, 
         "content": "Arthur Curry, the human-born heir to the underwater kingdom of Atlantis, goes on a quest to prevent a war between the worlds of ocean and land.", 
         "director":"James Wan", 
         "actor":"Jason Momoa, Amber Heard, Willem Dafoe", 
         "img": "posters/AquaMan.jpg",
         "netflix_link": "", 
         "amazon_link": "", 
         "preview": "https://www.youtube.com/watch?v=WDkg3h8PCVU"},
          
        {"title": "Inception", "likes": 15, "views": 10,
         "netflix_link": "https://www.netflix.com/title/70131314", 
         "amazon_link": "https://www.amazon.co.uk/Inception-Leonardo-DiCaprio/dp/B00G3ED5V8/ref=sr_1_1?s=instant-video&ie=UTF8&qid=1552986271&sr=1-1&keywords=inception",
         "preview": "https://www.youtube.com/watch?v=YoHD9XEInc0", 
         "director": "Christopher Nolan",
         "actor": "Leonardo DiCaprio, Joseph Gordon-Levitt, Ellen Page",
         "content": "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a CEO.",
         "img": "posters/Inception.jpg"},
         
         {"title": "Doctor Strange", "likes": 15, "views": 10,
         "netflix_link": "https://www.netflix.com/title/80108237", 
         "amazon_link": "https://www.amazon.co.uk/dp/B01M31APZ2?ref_=imdbref_tt_wbr_aiv&tag=imdbtag_tt_wbr_aiv-21",
         "preview": "https://www.youtube.com/watch?v=HSzx-zryEgM", 
         "director": "Scott Derrickson",
         "actor": " Benedict Cumberbatch, Chiwetel Ejiofor, Rachel McAdams",
         "content": "While on a journey of physical and spiritual healing, a brilliant neurosurgeon is drawn into the world of the mystic arts.",
         "img": "posters/DoctorStrange.jpg"},
        ]
    
    
    animation_movies = [
        {"title": "Rango", "views": 32, "likes": 16,
         "content": "Rango is an ordinary chameleon who accidentally winds up in the town of Dirt, a lawless outpost in the Wild West in desperate need of a new sheriff.",
         "netflix_link": "", 
         "amazon_link": "https://www.amazon.co.uk/dp/B00FKCYLHG?ref_=imdbref_tt_wbr_piv&tag=imdbtag_tt_wbr_piv-21", "preview": "https://www.youtube.com/watch?v=k-OOfW6wWyQ",
         "director": " Gore Verbinski", 
         "actor": "Johnny Depp, Isla Fisher, Timothy Olyphant", 
         "img": "posters/Rango.jpg"},
         
        {"title": "Spirited Away", "views": 30, "likes": 16, 
         "director": "Hayao Miyazaki, Kirk Wise", 
         "actor": "Daveigh Chase, Suzanne Pleshette, Miyu Irino",
         "content": "During her family's move to the suburbs, a sullen 10-year-old girl wanders into a world ruled by gods, witches, and spirits, and where humans are changed into beasts.",
         "netflix_link": "", 
         "amazon_link": "", 
         "preview": "https://www.youtube.com/watch?v=ByXuk9QqQkk", 
         "img": "posters/SpiritedAway.jpg"}
    ]
    
    
    comedy_movies = [
        {"title": "Jumanji: Welcome to the Jungle", "views": 40, "likes": 23,
         "content": "Four teenagers are sucked into a magical video game, and the only way they can escape is to work together to finish the game.",
         "netflix_link": "", "amazon_link": "https://www.amazon.co.uk/dp/B07C36VWQZ?ref_=imdbref_tt_wbr_aiv&tag=imdbtag_tt_wbr_aiv-21", 
         "preview": "https://www.youtube.com/watch?v=2QKg5SZ_35I",
         "director": "Jake Kasdan", 
         "actor": "Dwayne Johnson, Karen Gillan, Kevin Hart", 
         "img": "posters/Jumanji.jpg"},
         
        {"title": "The Grand Budapest Hotel", "views": 30, "likes": 20, 
         "director": "Wes Anderson", 
         "actor": " Ralph Fiennes, F. Murray Abraham, Mathieu Amalric",
         "content": "The adventures of Gustave H, a legendary concierge at a famous hotel from the fictional Republic of Zubrowka between the first and second World Wars, and Zero Moustafa, the lobby boy who becomes his most trusted friend.",
         "netflix_link": "https://www.netflix.com/title/70295915", 
         "amazon_link": "https://www.amazon.co.uk/dp/B00LBYDI6W?ref_=imdbref_tt_wbr_aiv&tag=imdbtag_tt_wbr_aiv-21", 
         "preview": "https://www.youtube.com/watch?v=1Fg5iWmQjwk", 
         "img": "posters/Budapest.jpg"}
    ]



    cats = {"Action": {"movies": action_movies},
            "Drama": {"movies": drama_movies},
            "Fantasy": {"movies": fantasy_movies},
            "Sci-Fi": {"movies": scifi_movies},
            "Animation": {"movies": animation_movies},
            "Comedy": {"movies": comedy_movies},
            }

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
