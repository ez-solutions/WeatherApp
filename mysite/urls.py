"""imozulu URL Configuration
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('app.urls')),
    url(r'^api/v1/', include('api.urls')),
]
