from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200)
    starring = models.CharField(max_length=200)
    summary = models.CharField(max_length=2000)
    genre = models.CharField(max_length=20)
    average_score = models.DecimalField(max_digits=5, decimal_places=3, default = 0.000)
    release_date = models.DateField(null=True)
    pub_date = models.DateTimeField('date published')

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

