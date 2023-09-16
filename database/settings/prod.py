import os
import dj_database_url
from .common import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = os.environ.get("DEBUG", "False").lower() == "true"

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(" ")

CSRF_TRUSTED_ORIGINS = ['https://super-mart2.herokuapp.com',
                        'https://localhost:3000', 'https://betcodes-fe.vercel.app/']

DATABASES = {
    'default': dj_database_url.config()
}
