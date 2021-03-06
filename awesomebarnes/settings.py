"""
Django settings for awesomebarnes project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_FILE = os.path.join(BASE_DIR, 'secret.txt')
try:
    SECRET_KEY = open(SECRET_FILE).read().strip()
except IOError:
    try:
        import random
        valid_chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
        SECRET_KEY = ''.join([
            random.SystemRandom().choice(valid_chars) for i in range(50)])
        secret = open(SECRET_FILE, 'w')
        secret.write(SECRET_KEY)
        secret.close()
    except IOError:
        Exception('Please create a %s file for secret key!' % SECRET_FILE)

# SECURITY WARNING: don't run with debug turned on in production!
try:
    from .local_settings import DEBUG
except ImportError:
    DEBUG = True


# Email settings
try:
    from .local_settings import ALLOWED_HOSTS
except ImportError:
    ALLOWED_HOSTS = []

try:
    from .local_settings import EMAIL_HOST
except ImportError:
    EMAIL_HOST = 'localhost'

try:
    from .local_settings import EMAIL_PORT
except ImportError:
    EMAIL_PORT = 25

try:
    from .local_settings import EMAIL_HOST_USER, EMAIL_HOST_PASSWORD
except ImportError:
    EMAIL_HOST_USER = None
    EMAIL_HOST_PASSWORD = None


# Application definition

INSTALLED_APPS = (
    'portfolio',
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'compressor',
    'filer',
    'mptt',
    'easy_thumbnails',
    'adminsortable',
    'django_nose',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'awesomebarnes.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'loaders': [
                ('django.template.loaders.cached.Loader', [
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                ]),
                'admin_tools.template_loaders.Loader',
            ]
        },
    },
]

WSGI_APPLICATION = 'awesomebarnes.wsgi.application'
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

try:
    from .local_settings import DATABASES
except ImportError:
    DATABASES = {
        'default':
            {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            }
        }


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
]

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Compressor settings
COFFEE_BIN = os.path.join(BASE_DIR, 'node_modules', '.bin', 'coffee')
LESSC_BIN = os.path.join(BASE_DIR, 'node_modules', '.bin', 'lessc')
SASS_BIN = os.path.join(BASE_DIR, 'node_modules', '.bin', 'sass')

COMPRESS_PRECOMPILERS = (
    ('text/coffeescript', COFFEE_BIN + ' --compile --stdio'),
    ('text/less', LESSC_BIN + ' {infile} {outfile}'),
    ('text/x-sass', SASS_BIN + ' {infile} {outfile}'),
    ('text/x-scss', SASS_BIN + ' --scss {infile} {outfile}'),
)

# Import local settings
try:
    from .local_settings import *
except ImportError:
    pass
