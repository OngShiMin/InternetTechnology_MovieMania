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



def index(request):
    category_list = Category.objects.order_by('-name')[:5]
    movie_list = Movie.objects.order_by('-views')[:5]
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
    try:
        movie = Movie.objects.get(slug=movie_title_slug)
        context_dict['movie'] = movie
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
                # Invalid form or forms - mistakes or sometihng else?
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
    form = UserProfileForm({'website': userprofile.website, 'picture': userprofile.picture})

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
        movie_list = Movie.objects.filter(name__istartswith=starts_with)

    if max_results > 0:
        if len(movie_list) > max_results:
            movie_list = movie_list[:max_results]
    return movie_list


def suggest_movie(request):
    movie_list = []
    starts_with = ''

    if request.method == 'GET':
        starts_with = request.GET['suggestion']
    movie_list = get_movie_list(8, starts_with)

    return render(request, 'moviemania/movies.html', {'movies': movie_list})






