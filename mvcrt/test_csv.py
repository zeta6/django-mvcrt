import os
import django

os.environ["DJANGO_SETTINGS_MODULE"] = 'mvcrt.settings'
django.setup()

from itertools import islice
import csv

from movie.models import MovieTest

with open('movie_csv.csv') as csvfile:
    reader = csv.reader(csvfile)
    batch_size = 10
    objs = (MovieTest(
        id=row[0],
        title=row[1],
        starring=row[2],
        summary=row[3],
        genre=row[4],
        average_score=row[5],
        release_date=row[6],
        pub_date=row[7]
        ) for row in reader)
    while True:
        batch = list(islice(objs, batch_size))
        if not batch:
            break
        MovieTest.objects.bulk_create(batch)
