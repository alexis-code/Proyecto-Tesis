from .base import *
from decouple import config
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config("NAME_DBPRUEBA"),
        'USER': 'root',
        'PASSWORD': config("PSSWD_DBPRUEBA"),
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}