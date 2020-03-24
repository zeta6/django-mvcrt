from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200)
    starring = models.CharField(max_length=200)
    summary = models.CharField(max_length=2000)
    genre = models.CharField(max_length=20)
    pub_date = models.DateTimeField('date published')