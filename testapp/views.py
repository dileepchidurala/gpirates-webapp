# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import generics
from testapp.serializers import *
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
class DisplayMovies(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class AddRequest(generics.CreateAPIView):
    serializer_class = requestSerializer

class Displayseries(generics.ListCreateAPIView):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer

class Displayapplications(generics.ListCreateAPIView):
    queryset = Applications.objects.all()
    serializer_class = ApplicationsSerializer

def index(request):
    return render(request, 'index.html')


def movies(request):
    return render(request, 'movies.html')


def series(request):
    return render(request, 'series.html')

def applications(request):
    return render(request, 'applications.html')

#
# def ModifySeries(request):
#
#
# def ModifyMovie(request):
#
