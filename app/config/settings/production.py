from .base import *

DEBUG = False

ALLOWED_HOSTS = [
    'localhost',
    '*.amazonaws.com',
    'pby.kr',
    'parkboyoung.kr',
]

WSGI_APPLICATION = 'config.wsgi.production.application'

AWS_SECRETS_MANAGER_SECRET_SECTION = 'project_crawler:production'

# s3 setting
AWS_REAGION = "ap-northeast-2"
AWS_STORAGE_BUCKET_NAME = 'selenium-crawler'

AWS_QUERYSTRING_AUTH = False

AWS_ACCESS_KEY_ID = secrets['AWS']['AWS_ACCESS_KEY']
AWS_SECRET_ACCESS_KEY = secrets['AWS']['AWS_SECRET_ACCESS_KEY']
AWS_LOCATION = '.static/'

AWS_S3_HOST = f's3.{AWS_REAGION}.amazonaws.com'
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

STATIC_URL = f"http://{AWS_S3_CUSTOM_DOMAIN}/.static/"
STATICFILES_STORAGE = 'config.storage_backend.StaticStorage'

MEDIA_URL = f"http://{AWS_S3_CUSTOM_DOMAIN}/.media/"
DEFAULT_FILE_STORAGE = 'config.storage_backend.MediaStorage'

# allauth SITE_ID 지정 안할경우 host domain으로 지정
SITE_ID = 4

# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': SECRETS['DATABASE']['DB_HOST'],
        'PORT': SECRETS['DATABASE']['DB_PORT'],
        'NAME': SECRETS['DATABASE']['DB_NAME'],
        'USER': SECRETS['DATABASE']['DB_USER'],
        'PASSWORD': SECRETS['DATABASE']['DB_PASSWORD']
    }
}
