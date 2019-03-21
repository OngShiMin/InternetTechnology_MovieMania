from django.test import TestCase
from moviemania.models import Category, Movie
from django.core.urlresolvers import reverse
from django.contrib.staticfiles import finders
from moviemania.admin import PageAdmin


class GeneralTests(TestCase):
    def test_serving_static_files(self):
        # In media, there is a .jpg file called 'title'
        # this should be found
        result = finders.find('images/title.jpg')
        self.assertIsNotNone(result)


class CategoryMethodTests(TestCase):
    def test_slug_line_creation(self):
        cat = Category(name='Random Category String')
        cat.save()
        self.assertEqual(cat.slug, 'random-category-string')


class MovieMethodTests(TestCase):
    def test_ensure_views_are_positive(self):
        cat = Category(name='test_cat')
        cat.save()
        movie = Movie(title='test', category=cat, views=-1, likes=0)
        movie.save()
        self.assertEqual((movie.views >= 0), True)

    def test_ensure_likes_are_positive(self):
        cat = Category(name='test_cat')
        cat.save()
        movie = Movie(title='test', category=cat, views=0, likes=-1)
        movie.save()
        self.assertEqual((movie.likes >= 0), True)

    def test_slug_line_creation_movie(self):
        cat = Category(name='test_cat')
        cat.save()
        movie = Movie(title='Random Category String', category=cat, views=0, likes=-1)
        movie.save()
        self.assertEqual(movie.slug, 'random-category-string')


class IndexViewTests(TestCase):
    def test_index_view_with_no_categories(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no categories present")
        self.assertQuerysetEqual(response.context['categories'], [])

    def test_index_view_with_no_movies(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no movies present")
        self.assertQuerysetEqual(response.context['movies'], [])


class AdminTests(TestCase):
    def test_admin_interface_page_view(self):
        self.assertIn('category', PageAdmin.list_display)
        self.assertIn('url', PageAdmin.list_display)


class PopulationTests(TestCase):
    def setUp(self):
        try:
            from populate_moviemania import populate
            populate()
        except ImportError:
            print('The module populate_rango does not exist')
        except NameError:
            print('The function populate() does not exist or is not correct')
        except:
            print('Something went wrong in the populate() function :-(')

    def get_category(self, name):

        from moviemania.models import Category
        try:
            cat = Category.objects.get(name=name)
        except Category.DoesNotExist:
            cat = None
        return cat

    def test_drama_cat_added(self):
        cat = self.get_category('Drama')
        self.assertIsNotNone(cat)

    def get_movie(self, title):
        from moviemania.models import Movie
        try:
            movie = Movie.objects.get(title=title)
        except Movie.DoesNotExist:
            movie = None
        return movie

    def test_titanic_movie_added(self):
        movie = self.get_movie('Titanic')
        self.assertIsNotNone(movie)

    def test_titanic_director_added(self):
        movie = self.get_movie('Titanic')
        director = movie.director
        self.assertIsNotNone(director)

    def test_titanic_image_added(self):
        movie = self.get_movie('Titanic')
        image = movie.img
        self.assertIsNotNone(image)
