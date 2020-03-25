from django.contrib import admin
from django.urls import include, path

from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(), name='home'),
    path('movie/', include('movie.urls')),
    path('main/', include('main.urls'))
]
