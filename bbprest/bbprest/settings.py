"""
Django settings for bbprest project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from platform import python_version
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# The real value is set in the local_settings.py
# local_settings.py is excluded from the git repository
# Place other important keys, passwords etc. in local_settings.py
# which is called at the end of settings.py

# I recommend setting a default/false value in settings.py
# and then overwriting in local_settings. This keeps the app
# functional if anyone clones the repository
# You can generate a new SECRET_KEY using tools such as
# http://www.miniwebtool.com/django-secret-key-generator/
#
SECRET_KEY = 'FAKE_VALUE_REAL_VALUE_SET_IN_LOCAL_SETTINGS'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

DEBUG_SETTINGS = True

ALLOWED_HOSTS = []
ADMINS = (
     ('Mark Scrimshire', 'mark@ekivemark.com'),
)

MANAGERS = ADMINS

APPLICATION_TITLE = "BlueButton Data Service"

if DEBUG_SETTINGS:
    print "Application: %s" % APPLICATION_TITLE
    print "Running on Python_version: %s" % python_version()
    print ""
    print "BASE_DIR:%s " % BASE_DIR

# Application definition

DEFAULT_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    'localflavor',
    'django_countries',
#    'provider',
#    'provider.oauth2',
    'oauth2_provider',
    'corsheaders',
    'rest_framework',
#    'fhir',
)

LOCAL_APPS = (
    'snippets',
#    'fhir_rest',
    'fhir_patient',
)

INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + LOCAL_APPS


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
)

ROOT_URLCONF = 'bbprest.urls'

WSGI_APPLICATION = 'bbprest.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
DBPATH = os.path.join(BASE_DIR, 'db/db.db')
if DEBUG_SETTINGS:
    print "DBPATH:",DBPATH


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': DBPATH,                  # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/New_York'
# TIME_ZONE = 'UTC'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'
# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

# Django Oauth Toolkit
# http://django-oauth-toolkit.readthedocs.org/en/latest/tutorial/tutorial_01.html
CORS_ORIGIN_ALLOW_ALL = True

# Oauth2_provider settings:
#OAUTH2_PROVIDER = {
#    # this is the list of available scopes
#    'SCOPES': ['read', 'write', 'groups']
#}

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, 'templates').replace('\\','/'),
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)
if DEBUG_SETTINGS:
    print "TEMPLATE_DIRS: %s" % TEMPLATE_DIRS



REST_FRAMEWORK = {
    #'FORMAT_SUFFIX_KWARG':'format',
    'URL_FORMAT_OVERRIDE':'_format',
#    'DEFAULT_AUTHENTICATION_CLASSES': (
#        'rest_framework.authentication.OAuth2Authentication',
#    ),

    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
#   'DEFAULT_PERMISSION_CLASSES': (
#       'rest_framework.permissions.IsAuthenticated',
#   ),
    'DEFAULT_RENDERER_CLASSES': (
        'fhir_patient.renderers.FHIRJRenderer',
        'fhir_patient.renderers.FHIRARenderer',
        'rest_framework.renderers.JSONRenderer',
#        'rest_framework.renderers.TemplateHTMLRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework.renderers.XMLRenderer',
    )

}


# Get Local Settings that you want to keep private.
# Make sure Local_settings.py is excluded from Git
try:
    from local_settings import *
except Exception as e:
    pass

if DEBUG_SETTINGS:
    print "SECRET_KEY:%s" % SECRET_KEY
    print "================================================================"
# SECURITY WARNING: keep the secret key used in production secret!

