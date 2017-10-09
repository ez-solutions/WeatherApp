from django.conf.urls import url

from . import views

app_name = 'api'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^cities/$', views.CityList.as_view()),
    url(r'^cities/(?P<pk>[0-9]+)/$', views.CityDetail.as_view()),
    url(r'^forecasts/$', views.ForecastList.as_view()),
    url(r'^forecasts/(?P<pk>[0-9]+)/$', views.ForecastDetail.as_view()),
]
