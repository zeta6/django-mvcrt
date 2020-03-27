from django.urls import path

from . import views

app_name = 'movie'
urlpatterns = [
    path('list', views.MovieListView.as_view(), name='list'),
    path('list/export_csv', views.export_csv, name='export_csv'),
    path('write', views.write, name='write'),
    path('post_write', views.post_write, name='post_write'),
    path('detail/<int:movie_id>/', views.detail, name='detail'),
    path('detail/<int:movie_id>/delete', views.delete, name='delete'),
    path('detail/<int:movie_id>/edit', views.edit, name='edit'),
]