# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.



class Movie(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to = 'pic_folder/')
    link = models.CharField(max_length=1000)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class SeriesImage(models.Model):
    series_name = models.CharField(max_length=128)
    image = models.ImageField()


class Series(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    count = models.IntegerField(default=0)
    link = models.CharField(max_length=1000)
    image = models.ForeignKey(SeriesImage)

    def __str__(self):
        return self.name


class RequestMe(models.Model):
    name  = models.CharField(max_length=100)
    requestDetail = models.CharField(max_length=1000)

    def __str__(self):
        return self.requestDetail