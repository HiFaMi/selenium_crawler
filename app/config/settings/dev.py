from .base import *

DEBUG = True

WSGI_APPLICATION = 'config.wsgi.dev.application'

INSTALLED_APPS += [
    'django_extensions',
]


# dev static media

STATIC_ROOT = os.path.join(BASE_DIR, '.static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, '.media')
MEDIA_URL = '/media/'

SITE_ID = 2

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
