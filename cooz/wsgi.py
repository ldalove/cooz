"""
WSGI config for cooz project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
import sys

path = '/home/ubuntu/cooz'
if path not in sys.path:
	sys.path.append(path)

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cooz.settings")

#application = get_wsgi_application()
application = DjangoWhiteNoise(get_wsgi_application())
