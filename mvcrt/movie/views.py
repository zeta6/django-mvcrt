import csv
import datetime

from django.utils import timezone
from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from django.urls import reverse
from django.http import HttpResponse

from .models import Movie

def export_csv_movie_list(request):
    genre = request.GET.get('genre')
    time_frame = request.GET.get('timeFrame')
    sort = request.GET.get('sort')
    title = request.GET.get('title')

    movies = Movie.movie_filter(genre, time_frame, sort, title)

    return movies

def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;filename=movie_list.csv'    
    
    writer = csv.writer(response)

    fields = Movie._meta.fields
    writer.writerow(field.column for field in fields)
    for movie in export_csv_movie_list(request):
        writer.writerow(x.value_from_object(movie) for x in fields)

    # xx = []
    # for x in fileds:
    #     xx.append x.value_from_object(movie)

    return response

class MovieListView(generic.ListView):
    template_name = 'movie/list.html'
    context_object_name = 'movie_list'

    def get_movie_list(self):
        genre = self.request.GET.get('genre')
        time_frame = self.request.GET.get('timeFrame')
        sort = self.request.GET.get('sort')
        title = self.request.GET.get('title')

        movies = Movie.movie_filter(genre, time_frame, sort, title)

        return movies



    def get_queryset(self):
        return None

    # def get_position(self):
    #     page = self.request.GET.get('page')
    #     if page == None or page =='':
    #         return 0
    #     else:
    #         return (int(page)-1) * 10

    def get_page_list(self):
        page_total = int(self.get_movie_list().count()/10) + 1
        page = self.request.GET.get('page')
        if page == None or page == '':
            page = 1
        else:
            page = int(page)

        start_page = page - 4
        if start_page < 1:
            start_page = 1

        end_page = page + 4
        if end_page > page_total:
            end_page = page_total

        return list(range(start_page,end_page+1))

    def get_context_data(self, **kwargs):
        page = self.request.GET.get('page')
        if page == None or page == '':
            page = 1

        page_total = int(self.get_movie_list().count()/10) + 1
        start_num = (int(page)-1) *10
        context = super().get_context_data(**kwargs)
        context['movie_list'] = self.get_movie_list()[start_num:start_num+10]
        context['movie_number'] = start_num
        context['pages'] = self.get_page_list()

        if self.get_page_list()[0] > 1:
            context['first_page'] = '1'
        if self.get_page_list()[-1] < page_total:
            context['last_page'] = page_total

        context['genre'] = self.request.GET.get('genre')
        context['timeFrame'] = self.request.GET.get('timeFrame')
        context['sort'] = self.request.GET.get('sort')
        title = self.request.GET.get('title')
        if title != None and title != '':
            context['title'] = title

        return context

    
# def list(request):
#     movie_list = Movie.objects.order_by('title')
#     context = {'movie_list': movie_list}
#     return render(request, 'movie/list.html', context)

def write(request):
    return render(request, 'movie/write.html')

def post_write(request):
    title = request.POST.get('title')
    genre = request.POST.get('genre')
    starring = request.POST.get('starring')
    summary = request.POST.get('summary')
    release_date = request.POST.get('release_date')
    m = Movie(title=title, starring=starring, summary=summary, genre=genre, average_score=0.00, release_date="2020-04-06", pub_date=timezone.now())
    m.save()
    movie_id = m.id
    return redirect(reverse('movie:detail', args=[movie_id]))

def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movie/detail.html', {'movie': movie})

def delete(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    movie.delete()
    return redirect(reverse('movie:list'))

def edit(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    movie.title = request.POST.get('title')
    movie.genre = request.POST.get('genre')
    movie.starring = request.POST.get('starring')
    movie.summary = request.POST.get('summary')
    movie.save()
    return redirect(reverse('movie:detail', args=[movie_id]))

