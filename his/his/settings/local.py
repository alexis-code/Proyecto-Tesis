from .base import *
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-klbj-cri92@ef0ok(hvny#x%yx(8b&ou4u^-ll)&9$ivwlet!*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_his_test',
        'USER': 'root',
        'PASSWORD': '$3Rv3r16',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}