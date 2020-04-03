import datetime

from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200)
    starring = models.CharField(max_length=200)
    summary = models.CharField(max_length=2000)
    genre = models.CharField(max_length=20)
    average_score = models.DecimalField(max_digits=5, decimal_places=3, default = 0.000)
    release_date = models.DateField(null=True)
    pub_date = models.DateTimeField('date published')

    @classmethod
    def movie_filter(cls, genre, time_frame, sort, title):
        movies = cls.objects    

        # filter
        if genre != None and genre != '':
            movies = movies.filter(genre=genre)
        
        if time_frame != None and time_frame != '':
            if time_frame == 'last90days':
                movies = movies.filter(release_date__lte=datetime.date.today(), release_date__gt=datetime.date.today()-datetime.timedelta(days=90))
            else:
                movies = movies.filter(release_date__year=time_frame)

        if title != None and title != '':
            movies = movies.filter(title__icontains=title)

        # sort
        if sort == None or sort == '':
            movies = movies.order_by('-release_date')
        elif sort == 'A_Z':
            movies = movies.order_by('title')
        elif sort == 'Z_A':
            movies = movies.order_by('-title')
        elif sort == 'Score':
            movies = movies.order_by('-average_score')

        return movies

    class Meta:
        db_table = "movies"



class MovieTest(models.Model):
    title = models.CharField(max_length=200)
    starring = models.CharField(max_length=200)
    summary = models.CharField(max_length=2000)
    genre = models.CharField(max_length=20)
    average_score = models.DecimalField(max_digits=5, decimal_places=3, default = 0.000)
    release_date = models.DateField(null=True)
    pub_date = models.DateTimeField('date published')

    class Meta:
        db_table = "movie_test"

