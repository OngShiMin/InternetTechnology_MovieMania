from django.conf.urls import url
from moviemania import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.show_category, name='show_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/(?P<movie_title_slug>[\w\-]+)/$', views.show_movie, name='show_movie'),
    url(r'search/$', views.search, name='search'),
    url(r'^register_profile/$', views.register_profile, name='register_profile'),
    url(r'^profile/(?P<username>[\w\-]+)/$', views.profile, name='profile'),
    url(r'^profiles/$', views.list_profiles, name='list_profiles'),
    url(r'^suggest/$', views.suggest_movie, name='suggest_movie'),
]
