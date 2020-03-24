from django.shortcuts import get_object_or_404, render

from .models import Movie


def list(request):
    movie_list = Movie.objects.order_by('title')[:10]
    context = {'movie_list': movie_list}
    return render(request, 'movie/list.html', context)

def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movie/detail.html', {'movie': movie})
    