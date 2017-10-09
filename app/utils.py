from __future__ import unicode_literals
from functools import wraps

from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect


def require_login(func):
    @wraps(func)
    def decorator(instance, request, *args, **kwargs):
        if 'user' not in  request.session:
            messages.add_message(request, messages.ERROR, 'Please login first')
            request.session.flush();
            return HttpResponseRedirect(reverse('app:login'))
        return func(instance, request, *args, **kwargs)

    return decorator
