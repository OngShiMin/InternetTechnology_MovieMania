from django import forms
from django.contrib.auth.models import User
from moviemania.models import UserProfile
from moviemania.models import Movie


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    picture = forms.ImageField(required=False)
    favorites = forms.ModelMultipleChoiceField(queryset=Movie.objects.all())

    class Meta:
        model = UserProfile
        exclude = ('user',)

