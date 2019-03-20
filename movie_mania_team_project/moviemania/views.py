from django.shortcuts import render
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from moviemania.forms import UserForm, UserProfileForm
from moviemania.models import Category, Movie, UserProfile
from registration.backends.simple.views import RegistrationView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from moviemania.webhose_search import run_query
# =============================================================================
# from social_django.models import UserSocialAuth
# =============================================================================


def index(request):
    category_list = Category.objects.order_by('-name')
    movie_list = Movie.objects.order_by('-likes')[:12]
    
    context_dict = {'categories': category_list, 'movies': movie_list}
    
    response = render(request, 'moviemania/index.html', context_dict)
    return response


def show_category(request, category_name_slug):
    # Create a context dictionary which we can pass
    # to the template rendering engine.
    context_dict = {}
    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        category = Category.objects.get(slug=category_name_slug)
        # Retrieve all of the associated pages.
        # Note that filter() will return a list of page objects or an empty list
        movies = Movie.objects.filter(category=category)
        # Adds our results list to the template context under name pages.
        context_dict['movies'] = movies
        # We also add the category object from
        # the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['category'] = category
    except Category.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything -
        # the template will display the "no category" message for us.
        context_dict['category'] = None
        context_dict['movies'] = None
        # Go render the response and return it to the client.
    return render(request, 'moviemania/category.html', context_dict)


def show_movie(request, category_name_slug, movie_title_slug):
    context_dict = {}
    context_dict['show_like_button'] = False
    context_dict['show_watchlist_button'] = False
    context_dict['show_remove_favorites_button'] = False
    context_dict['show_remove_watchlist_button'] = False

    try:
        movie = Movie.objects.get(slug=movie_title_slug)
        context_dict['movie'] = movie

        if request.user.is_authenticated():
            profile = UserProfile.objects.get(user=request.user)
            favorites = profile.favorites.all()
            watchlist = profile.watchlist.all()

            if movie not in favorites:
                context_dict['show_like_button'] = True

            if movie not in watchlist:
                context_dict['show_watchlist_button'] = True

            if movie in favorites:
                context_dict['show_remove_favorites_button'] = True

            if movie in watchlist:
                context_dict['show_remove_watchlist_button'] = True


    except Movie.DoesNotExist:
        context_dict['movie'] = None
        context_dict['category'] = None

    return render(request, 'moviemania/movie.html', context_dict)


def register(request):
    # Boolean is set to false initially
    # changes to true when registration succeeds
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

                profile.save()
                registered = True
            else:
                # Invalid form or forms - mistakes or something else?
                # Print problems to the terminal
                print(user_form.errors, profile_form.errors)
        else:
            user_form = UserForm()
            profile_form = UserProfileForm()

        # Render the template depending on the context
        return render(request,
                      'moviemania/register.html',
                      {'user_form': user_form,
                       'profile_form': profile_form,
                       'registered': registered})


def search(request):
    result_list = []

    if request.method == 'POST':
        query = request.POST['query'].strip()
        if query:
            # Run the webhose search function to get the results list
            result_list = run_query(query)

    return render(request, 'moviemania/search.html', {'result_list': result_list})


@login_required
def register_profile(request):
    form = UserProfileForm()
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()

            return redirect('index')
        else:
            print(form.errors)

    context_dict = {'form': form}

    return render(request, 'moviemania/profile_registration.html', context_dict)


class MovieManiaRegistrationView(RegistrationView):
    def get_success_url(self, user):
        return reverse('register_profile')


@login_required
def profile(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return redirect('index')

    userprofile = UserProfile.objects.get_or_create(user=user)[0]
    form = UserProfileForm({'website': userprofile.website, 'picture': userprofile.picture, 'favorites': userprofile.favorites, 'watchlist': userprofile.watchlist})
    form.fields['favorites'].queryset = userprofile.favorites.all()
    form.fields['watchlist'].queryset = userprofile.watchlist.all()
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=userprofile)
        if form.is_valid():
            form.save(commit=True)
            return redirect('profile', user.username)
        else:
            print(form.errors)

    return render(request, 'moviemania/profile.html', {'userprofile': userprofile, 'selecteduser': user, 'form': form })


@login_required
def list_profiles(request):
    userprofile_list = UserProfile.objects.all()
    return render(request, 'moviemania/list_profiles.html', {'userprofile_list': userprofile_list})


def get_movie_list(max_results=0, starts_with=''):
    movie_list = []
    if starts_with:
        movie_list = Movie.objects.filter(title__istartswith=starts_with)

    if max_results > 0:
        if len(movie_list) > max_results:
            movie_list = movie_list[:max_results]
    return movie_list


def get_director_list(max_results=0, starts_with=''):
    director_list = []
    if starts_with:
        director_list = Movie.director.filter(title__istartswith=starts_with)

    if max_results > 0:
        if len(director_list) > max_results:
            movie_list = director_list[:max_results]
    return director_list


def get_actor_list(max_results=0, starts_with=''):
    actor_list = []
    if starts_with:
        actor_list = Movie.actor.filter(title__istartswith=starts_with)

    if max_results > 0:
        if len(actor_list) > max_results:
            movie_list = actor_list[:max_results]
    return actor_list


def suggest_movie(request):
    movie_list = []
    starts_with = ''

    if request.method == 'GET':
        starts_with = request.GET['suggestion']
    movie_list = get_movie_list(8, starts_with)
    return render(request, 'moviemania/movies.html', {'movies': movie_list})


@login_required
def like_movie(request):
    movie_id = None
    if request.method == 'GET':
        movie_id = request.GET['movie_id']
    likes = 0
    if movie_id:
        movie = Movie.objects.get(id=int(movie_id))
        if movie:
            likes = movie.likes + 1
            movie.likes = likes
            movie.save()

            # Get user details
            user = request.user
            profile = UserProfile.objects.get(user=user)
            profile.favorites.add(movie)
            profile.save()

    return HttpResponse(likes)


@login_required
def add_to_watchlist(request):
    movie_id = None
    if request.method == 'GET':
        movie_id = request.GET['movie_id']
    watchlist = 0
    if movie_id:
        movie = Movie.objects.get(id=int(movie_id))
        if movie:
            watchlist = movie.watchlistCount + 1
            movie.watchlistCount = watchlist
            movie.save()

            # Get user details
            user = request.user
            profile = UserProfile.objects.get(user=user)
            profile.watchlist.add(movie)
            profile.save()

    return HttpResponse(watchlist)


# =============================================================================
# @login_required
# def home(request):
#     return render(request, 'core/home.html')
# 
# 
# @login_required
# def settings(request):
#     user = request.user
#     
#     try:
#         twitter_login = user.social_auth.get(provider='twitter')
#     except UserSocialAuth.DoesNotExist:
#         twitter_login = None
#         
#     can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())
#     
#     return render(request, 'core/settings.html', {
#         'twitter_login': twitter_login,
#         'can_disconnect': can_disconnect
#     })
#     
# 
# @login_required
# def password(request):
#     if request.user.has_usable_password():
#         PasswordForm = PasswordChangeForm
#     else:
#         PasswordForm = AdminPasswordChangeForm
#         
#     if request.method == 'POST':
#         form = PasswordForm(request.user, request.POST)
#         if form.is_valid():
#             form.save()
#             update_session_auth_hash(request, form.user)
#             messages.success(request, 'Your password was successfully update!')
#             return redirect('password')
#         else:
#             messages.error(request, 'Please correct error below.')
#     else:
#         form = PasswordForm(request.user)
#     return render(request, 'core/password.html', {'form': form})
# =============================================================================


@login_required
def remove_from_watchlist(request):
    movie_id = None
    if request.method == 'GET':
        movie_id = request.GET['movie_id']
    watchlist = 0
    if movie_id:
        movie = Movie.objects.get(id=int(movie_id))
        if movie:
            watchlist = movie.watchlistCount - 1
            movie.watchlistCount = watchlist
            movie.save()

            # Get user details
            user = request.user
            profile = UserProfile.objects.get(user=user)
            profile.watchlist.remove(movie)
            profile.save()

    return HttpResponse(watchlist)


@login_required
def remove_from_favorites(request):
    movie_id = None
    if request.method == 'GET':
        movie_id = request.GET['movie_id']
    likes = 0
    if movie_id:
        movie = Movie.objects.get(id=int(movie_id))
        if movie:
            likes = movie.likes - 1
            movie.likes = likes
            movie.save()

            # Get user details
            user = request.user
            profile = UserProfile.objects.get(user=user)
            profile.favorites.remove(movie)
            profile.save()

    return HttpResponse(likes)

