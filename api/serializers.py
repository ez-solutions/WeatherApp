from rest_framework import serializers

from app import models as app_models


class CitySerializer(serializers.ModelSerializer):
    forecasts = serializers.PrimaryKeyRelatedField(
        many=True, queryset=app_models.Forecast.objects.all())

    class Meta:
        model = app_models.City
        fields = ('id', 'name', 'code', 'forecasts')


class ForecastSerializer(serializers.ModelSerializer):

    class Meta:
        model = app_models.Forecast
