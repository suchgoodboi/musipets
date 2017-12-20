"""
WSGI config for pets project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
"""

from os import environ

environ.setdefault("DJANGO_SETTINGS_MODULE", "pets.settings.dev")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
