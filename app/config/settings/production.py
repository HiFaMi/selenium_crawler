from .base import *

DEBUG = False

ALLOWED_HOSTS = [
    '*',
]

WSGI_APPLICATION = 'config.wsgi.production.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': secrets['DATABASE']['DB_HOST'],
        'PORT': secrets['DATABASE']['DB_PORT'],
        'NAME': secrets['DATABASE']['DB_NAME'],
        'USER': secrets['DATABASE']['DB_USER'],
        'PASSWORD': secrets['DATABASE']['DB_PASSWORD'],
    }
}
