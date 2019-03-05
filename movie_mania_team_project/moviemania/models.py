from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
#from django.core.files.storage import FileSystemStorage

#fs = FileSystemStorage(location='/media/posters')


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
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
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

    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        self.category.slug = slugify(self.category.name)
        self.slug = slugify(self.title)
        super(Movie, self).save(*args, **kwargs)

#    img = models.ImageField(storage=fs)



    def __str__(self):
        return self.title

