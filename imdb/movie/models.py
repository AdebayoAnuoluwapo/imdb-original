from django.db import models

# Create your models here.

ACTION = 'action'
DRAMA = 'drama'
COMEDY = 'comedy'
ROMANCE = 'romance'

CATEGORY_CHOICES = (
    (ACTION, 'Action'),
    (DRAMA, 'Drama'),
    (COMEDY, 'Comedy'),
    (ROMANCE, 'Romance'),
)

LANGUAGE_CHOICES = (
    ('english','ENGLISH'),
    ('german','GERMAN'),
    ('russian','RUSSIAN'),
)

STATUS_CHOICES = (
    ('MW','MOST WATCHED'),
    ('RA','RECENTLY ADDED'),
    ('TR','TOP RATED'),
)

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)
    image = models.ImageField(upload_to='movies')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=10)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=7)
    status = models.CharField(choices=STATUS_CHOICES, max_length=2)
    cast = models.CharField(max_length=100) 
    year_of_production = models.DateField()
    views_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title   


LINK_CHOICES = (
    ('D','DOWNLOAD_LINK'),
    ('W','WATCH_LINK')
)


class MovieLinks(models.Model):
    movie = models.ForeignKey(Movie, related_name='movie_watch_link', on_delete=models.CASCADE)
    movie_link_choice = models.CharField(choices=LINK_CHOICES, max_length=1)
    links = models.URLField()
    
    def __str__(self):
        return str(self.movie) 


    
