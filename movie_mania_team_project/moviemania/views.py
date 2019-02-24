from django.shortcuts import render
from django.http import HttpResponse
from moviemania.forms import UserForm, UserProfileForm
from registration.backends.simple.views import RegistrationView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def index(request):
    response = render(request, 'moviemania/index.html')
    return response



class MovieManiaRegistrationView(RegistrationView):
    def get_success_url(self, user):
        return '/moviemania'


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

