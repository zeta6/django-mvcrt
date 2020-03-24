from django.urls import path

from . import views

urlpatterns = [
    path('list', views.list, name='list'),
    path('<int:movie_id>/', views.detail, name='detail'),
]