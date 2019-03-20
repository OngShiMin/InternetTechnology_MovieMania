from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify



class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Movie(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    watchlistCount = models.IntegerField(default=0)
    img = models.ImageField(upload_to='posters', blank=True)
    director = models.CharField(max_length=128, blank=True)
    actor = models.CharField(max_length=128, blank=True)
    content = models.TextField(blank=True)
    amazon_link = models.URLField(blank=True)
    netflix_link = models.URLField(blank=True)
    preview = models.URLField(blank=True)
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        self.category.slug = slugify(self.category.name)
        self.slug = slugify(self.title)
        super(Movie, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User)

    # The additional attributes we wish to include
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    favorites = models.ManyToManyField(Movie, blank=True, related_name="likes_movie")
    watchlist = models.ManyToManyField('Movie', blank=True, related_name="watchlistCount_movie")

    # Override the __unicode__() method to return out something meaningful

    def __str__(self):
        return self.user.username


class Comments(models.Model):
    comment_content = models.CharField(max_length=128)
    score = models.IntegerField()
    movie = models.ForeignKey(Movie)
    user = models.ForeignKey(User)    
    
    def __str__(self):
        return self.comment_content

