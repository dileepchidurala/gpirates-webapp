from django.conf.urls import url
from . import views

app_name = 'test'

urlpatterns = [
    url(r"^$", views.index, name='movies'),
    url(r"^movies_list/$", views.DisplayMovies.as_view(), name='test_movielilst'),
    url(r"^movies/$", views.movies, name='test_movies'),
    url(r"^series/$", views.series, name='test_series'),
    url(r"^series_list/$", views.Displayseries.as_view(), name='test_series'),
    url(r"^addrequest/$", views.AddRequest.as_view(), name='test_series'),
]
