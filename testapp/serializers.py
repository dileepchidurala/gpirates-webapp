from rest_framework import serializers
from testapp.models import *


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ("name" , "description" ,"image",'link', "count" )


class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = ("name" , "description" ,"count",'image', "link" )


class requestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestMe
        fields = ("name","requestDetail")