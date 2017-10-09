from __future__ import unicode_literals
from django.conf import settings
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView, FormView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.http import HttpResponseRedirect

from . import forms
from . import models
from . import utils
from .log import logger


class IndexView(TemplateView):
    template_name = 'app/index.html'


class RegisterView(CreateView):
    template_name = 'app/register.html'
    form_class = forms.RegisterForm
    success_url = '/login'

    def form_valid(self, form):
        messages.add_message(
            self.request, messages.INFO, 'You have been registered, please login')
        return super(RegisterView, self).form_valid(form)


class LoginView(FormView):
    template_name = 'app/login.html'
    form_class = forms.LoginForm
    success_url = '/dashboard'

    def form_valid(self, form):
        self.request.session.set_expiry(0);
        email = form.cleaned_data['email']
        user = models.User.objects.filter(email=email).values()

        if user:
            logger.info("Logging in %s", user)
            self.request.session['user'] = dict(user[0])

        return super(LoginView, self).form_valid(form)


class LogoutView(TemplateView):

    def get(self, request, *args, **kwargs):
        logger.info("Logging out %s", self.request.user)
        self.request.session.flush();
        messages.add_message(request, messages.INFO, 'You have been logged out')
        return HttpResponseRedirect(reverse('app:index'))


class DashboardView(ListView):
    template_name = 'app/dashboard.html'
    paginate_by = 3

    @utils.require_login
    def get(self, request, *args, **kwargs):
        return super(DashboardView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        user = models.User.objects.get(id=self.request.session['user']['id'])
        
        if user.city is None:
            code = settings.APP['default_city']['cityId']
        else:
            code = user.city.code
        logger.info("Retrieving forecast data for user: %s", user)
        queryset = models.Forecast.objects.filter(city__code=code)
        return queryset
