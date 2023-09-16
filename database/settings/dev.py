from .common import *
import dj_database_url

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-09$^3526099-7d25k*j!c9r6i^c45j9+19^kss3c$t_o1q3-e!'

DEBUG = True

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
# _psycopg2

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'my_database',
        'HOST': 'localhost',
        'USER': 'postgres',
        'PASSWORD': 'Agtm2486'

    }
}

DATABASES['default'] = dj_database_url.parse(
    "postgres://my_database_7n45_user:6oVxJpAGkkzIuuuz9DKGVFDOtzd3VKLf@dpg-ck2l49vqj8ts73f4nqjg-a.oregon-postgres.render.com/my_database_7n45")
