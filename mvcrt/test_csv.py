import csv

from movie.models import MovieTest

with open('movie_csv.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        created = MovieTest.objects.get_or_create(
            id=row[0],
            title=row[1],
            starring=row[2],
            summary=row[3],
            genre=row[4],
            average_score=row[5],
            release_date=row[6],
            pub_date=row[7]
            )

