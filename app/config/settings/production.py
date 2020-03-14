from .base import *

DEBUG = False

ALLOWED_HOSTS = [
    'localhost',
    '*.amazonaws.com',
    'pby.kr',
    'parkboyoung.kr',
]

WSGI_APPLICATION = 'config.wsgi.production.application'

# Database

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
