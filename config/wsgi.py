"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os  #Is file mein iska use environment variables access karne ke liye hota hai.

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings') #Django ko bataya ja raha hai ki project 
#settings config.settings, yaani config/settings.py, mein hain.

application = get_wsgi_application()  #Production server is callable ko use karke requests Django tak pahunchata
#hai aur responses receive karta hai.
