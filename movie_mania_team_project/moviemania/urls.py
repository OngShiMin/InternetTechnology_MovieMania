from django.conf.urls import url
from moviemania import views
from django.contrib.auth import views as auth_views
from django.conf.urls import include
#from mysite.core import views as core_views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.show_category, name='show_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/(?P<movie_title_slug>[\w\-]+)/$', views.show_movie, name='show_movie'),
    url(r'search/$', views.search, name='search'),
    url(r'^register_profile/$', views.register_profile, name='register_profile'),
    url(r'^profile/(?P<username>[\w\-]+)/$', views.profile, name='profile'),
    url(r'^profiles/$', views.list_profiles, name='list_profiles'),
    url(r'^suggest_movie/$', views.suggest_movie, name='suggest_movie'),
    url(r'^like/$', views.like_movie, name='like_movie'),
    url(r'^watchlist/$', views.add_to_watchlist, name='add_to_watchlist'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
# =============================================================================
#     url(r'^settings/$', core_views.settings, name='settings'),
#     url(r'^settings/password/$', core_views.password, name='password'),
# =============================================================================

]
