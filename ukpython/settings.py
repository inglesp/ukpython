"""
Django settings for ukpython project.

Generated by 'django-admin startproject' using Django 1.10.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# This does not need to be kept secret, since it is not used to protect
# anything in the static site.
SECRET_KEY = 'secret'

# SECURITY WARNING: This should be False when the site is built to ensure we
# don't accidentally leak information in error pages.  This has the added
# effect of massively speeding up the build, since LESS compilation no longer
# happens on every request!
DEBUG = bool(os.getenv('DEBUG', False))

# This is fine.
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'ukpython',

    'django_amber',
    'markdown_deux',
    'compressor',

    # These two apps are required for Django to work properly, even though we
    # don't use them directly.
    'django.contrib.auth',
    'django.contrib.contenttypes',

    'django.contrib.staticfiles',
]

MIDDLEWARE_CLASSES = [
]

ROOT_URLCONF = 'ukpython.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ukpython.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'UTC'

USE_TZ = True


# Formatting

DATE_FORMAT = 'jS F Y'  # eg 25th December 2016


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'media')
]
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)


# Markdown

MARKDOWN_DEUX_STYLES = {
    'default': {
        'safe_mode': False,  # This means we don't escape HTML tags in Markdown
    }
}


# Django Amber

# TODO
# DJANGO_AMBER_CNAME = ''


# Django Compressor

COMPRESS_PRECOMPILERS = (
    ('text/less', 'lessc {infile} {outfile}'),
)


# API key for retrieving events from meetup.com
# See https://secure.meetup.com/meetup_api/key/.

MEETUP_API_KEY = os.getenv('MEETUP_API_KEY', None)
