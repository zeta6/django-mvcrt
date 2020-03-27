import datetime

from django.shortcuts import get_object_or_404, render
from django.views import generic

from movie.models import Movie

class HomeView(generic.ListView):
    template_name = 'main/home.html'

    def get_queryset(self):
        return None
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #available_now release_date 오늘이전 최신순
        context['available_now'] = Movie.objects.filter(release_date__lte=datetime.date.today()).order_by('-release_date')[:10]
        #upcoming_release release_date 내일 이후 오늘에 가까운 순
        context['upcoming_release'] = Movie.objects.filter(release_date__gt=datetime.date.today()).order_by('release_date')[:10]
        #recently_popular release_date 30이전~오늘 score_average 높은 순
        context['recently_popular'] = Movie.objects.filter(release_date__lte=datetime.date.today(), release_date__gt=datetime.date.today()-datetime.timedelta(days=30)).order_by('-average_score')[:10]
        return context