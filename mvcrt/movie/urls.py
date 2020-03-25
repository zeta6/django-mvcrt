from django.urls import path

from . import views

app_name = 'movie'
urlpatterns = [
    path('list', views.ListView.as_view(), name='list'),
    path('<int:movie_id>/', views.detail, name='detail'),
]