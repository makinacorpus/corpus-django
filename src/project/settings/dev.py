# -*- coding: utf-8 -*-
import logging

from django.utils import six

from .base import *  # noqa


SECRET_KEY = 'dev-dev-dev-dev-dev-dev-dev'

ALLOWED_HOSTS = []
DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INSTALLED_APPS += (  # noqa
    'debug_toolbar',
    'django_extensions',
)

MIDDLEWARE += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

INTERNAL_IPS = ('127.0.0.1',)  # Used by app debug_toolbar

# Add the Python core NullHandler to be available when needed
LOGGING['handlers']['null'] = {  # noqa
    'level': logging.NOTSET,
    'class': 'logging.NullHandler',
}

# Force every loggers to use console handler only. Note that using 'root'
# logger is not enough if children don't propage.
for logger in six.itervalues(LOGGING['loggers']):  # noqa
    logger['handlers'] = ['console']
# Log every level.
LOGGING['handlers']['console']['level'] = logging.NOTSET  # noqa


try:
    from .local import *  # noqa
except ImportError:
    pass
