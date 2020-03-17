from .base import *

DEBUG = False

ALLOWED_HOSTS = [
    '*.amazonaws.com',
    'pby.kr',
    'parkboyoung.kr',
]

WSGI_APPLICATION = 'config.wsgi.production.application'

# s3 setting
AWS_REAGION = "ap-northeasr-2"
AWS_STORAGE_BUCKET_NAME = 'selenium-crawler'

AWS_QUERYSTRING_AUTH = False

AWS_ACCESS_KEY_ID = secrets['AWS']['AWS_ACCESS_KEY']
AWS_SECRET_ACCESS_KEY = secrets['AWS']['AWS_SECRET_ACCESS_KEY']
AWS_LOCATION = '.static/'

AWS_S3_HOST = f's3.{AWS_REAGION}.amazonaws.com'
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_S3_MEDIA_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_REAGION}.amazonaws.com'

STATIC_URL = f"http://{AWS_S3_CUSTOM_DOMAIN}/.static/"
STATICFILES_STORAGE = 'config.storage_backend.StaticStorage'

MEDIA_URL = f"http://{AWS_S3_MEDIA_DOMAIN}/.media/"
DEFAULT_FILE_STORAGE = 'config.storage_backend.MediaStorage'

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
