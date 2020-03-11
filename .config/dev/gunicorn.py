daemon = False
chdir = '/srv/project/app'
bind = 'unix:/tmp/app.sock'
workers = 1
threads = 1
tomeout = 60
accesslog = '/var/log/gunicorn/app-access.log'
errorlog = '/var/log/gunicorn/app-error.log'
capture_output = True
raw_env = [
    'DJANGO_SETTINGS_MODULE=config.settings.dev',
]


