from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)

    # The additional attributes we wish to include
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile:images', blank=True)

    # Override the __unicode__() method to return out something meaningful
    def __str__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Movie(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

