from __future__ import unicode_literals
import os
import logging
from django.conf import settings
# from logging.config import dictConfig


LOG_DIR = os.path.join(settings.BASE_DIR, 'mysite', 'log')

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create a file handler
app_log = os.path.join(LOG_DIR, 'app.log')
handler = logging.FileHandler(app_log)
handler.setLevel(logging.INFO)

# create a logging format
formatter = logging.Formatter(
    '[%(asctime)s] p%(process)s {%(pathname)s:%(lineno)d [%(funcName)s]} %(levelname)s - %(message)s', '%m-%d %H:%M:%S'
)
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)
