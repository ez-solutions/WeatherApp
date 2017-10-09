from __future__ import unicode_literals
from django.conf.urls import url
from django.core.urlresolvers import reverse

from . import views

app_name = 'app'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^register$', views.RegisterView.as_view(), name='register'),
    url(r'^login$', views.LoginView.as_view(), name='login'),
    url(r'^logout$', views.LogoutView.as_view(), name='logout'),
    url(r'^dashboard$', views.DashboardView.as_view(), name='dashboard'),
]
