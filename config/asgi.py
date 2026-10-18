"""
ASGI config for config project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os  #provides functionality for interacting with the operating system, including environment variables.

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings') #Sets the settings-module environment 
#variable if it isn't already set.

application = get_asgi_application()  #Initializes Django's ASGI application and exposes it to the server.
