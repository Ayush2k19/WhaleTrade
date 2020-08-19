"""
WSGI config for WhaleTrade project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
import math


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WhaleTrade.settings')

application = get_wsgi_application()