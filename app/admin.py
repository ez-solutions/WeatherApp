from __future__ import unicode_literals
from django.contrib import admin

from . import models


class ForecastInline(admin.TabularInline):
    model = models.Forecast


class CityAdmin(admin.ModelAdmin):
    inlines = (ForecastInline,)


class UserAdmin(admin.ModelAdmin):
    list_display = ('__str__',)


admin.site.register(models.User, UserAdmin)
admin.site.register(models.City, CityAdmin)
