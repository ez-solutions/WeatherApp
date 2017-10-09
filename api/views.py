from rest_framework import generics, permissions

from django.views.generic import TemplateView

from app import models as app_models

from . import serializers


class IndexView(TemplateView):
    template_name = 'api/index.html'


class CityList(generics.ListAPIView):
    queryset = app_models.City.objects.all()
    serializer_class = serializers.CitySerializer
    permission_classes = (permissions.IsAuthenticated,)


class CityDetail(generics.RetrieveAPIView):
    queryset = app_models.City.objects.all()
    serializer_class = serializers.CitySerializer
    permission_classes = (permissions.IsAuthenticated,)


class ForecastList(generics.ListCreateAPIView):
    queryset = app_models.Forecast.objects.all()
    serializer_class = serializers.ForecastSerializer
    permission_classes = (permissions.IsAuthenticated,)


class ForecastDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = app_models.Forecast.objects.all()
    serializer_class = serializers.ForecastSerializer
    permission_classes = (permissions.IsAuthenticated,)
