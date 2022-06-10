"""
WSGI config for R7_generic_api_view_and_mixins project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'R7_generic_api_view_and_mixins.settings')

application = get_wsgi_application()