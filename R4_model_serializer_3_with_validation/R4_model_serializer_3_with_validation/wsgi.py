"""
WSGI config for R4_model_serializer_3_with_validation project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'R4_model_serializer_3_with_validation.settings')

application = get_wsgi_application()
