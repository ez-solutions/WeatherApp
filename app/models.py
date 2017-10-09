from __future__ import unicode_literals
from passlib.hash import sha256_crypt

from django.db import models


class City(models.Model):
    name = models.CharField(max_length=255)
    # This is the cityId for fetching the city data from weather.news24.com
    code = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'city'
        verbose_name_plural = 'cities'

    def __unicode__(self):
        return "{0} {1}".format(self.name, self.code)


class User(models.Model):
    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def is_authentic(self, password):
        return sha256_crypt.verify(password, self.password)

    def __unicode__(self):
        return self.email


class Forecast(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='forecasts')
    day = models.CharField(unique=True,max_length=255)
    description = models.CharField(max_length=255)
    sky_description = models.CharField(max_length=255, blank=True, null=True)
    precipitation_description = models.CharField(max_length=255, blank=True, null=True)
    precipitation_probability = models.IntegerField(blank=True, null=True)
    temperature_description = models.CharField(max_length=255, blank=True, null=True)
    temperature_high = models.IntegerField(blank=True, null=True)
    temperature_low = models.IntegerField(blank=True, null=True)
    uv_description = models.CharField(max_length=255, blank=True, null=True)
    air_description = models.CharField(max_length=255, blank=True, null=True)
    wind_speed = models.IntegerField(blank=True, null=True)
    wind_direction_description = models.CharField(max_length=255, blank=True, null=True)
    dew_point = models.CharField(max_length=255, blank=True, null=True)
    humidity = models.CharField(max_length=255, blank=True, null=True)
    comfort = models.CharField(max_length=255, blank=True, null=True)
    visibility = models.CharField(max_length=255, blank=True, null=True)
    rainfall = models.CharField(max_length=255, blank=True, null=True)
    snowfall = models.CharField(max_length=255, blank=True, null=True)
    icon_name = models.CharField(max_length=255, blank=True, null=True)
    beaufort_description = models.CharField(max_length=255, blank=True, null=True)
