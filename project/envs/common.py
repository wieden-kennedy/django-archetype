from os.path import abspath, join, dirname
from sys import path
from envs.aws_keys import *

PROJECT_ROOT = abspath(join(dirname(__file__), "../"))
APPS_DIR = abspath(join(PROJECT_ROOT, "apps"))
path.insert(0, PROJECT_ROOT)
path.insert(0, APPS_DIR)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'project.sqlite3',            # Or path to database file if using sqlite3.
        'USER': 'root',                       # Not used with sqlite3.
        'PASSWORD': '',                   # Not used with sqlite3.
        'HOST': '',                       # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                       # Set to empty string for default. Not used with sqlite3.
    }
}

TIME_ZONE = 'America/Vancouver'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = False
USE_L10N = False


MEDIA_ROOT = join(PROJECT_ROOT, "media_root")
MEDIA_URL = ''

STATIC_ROOT = join(PROJECT_ROOT, "collected_static")
STATIC_URL = '/static/'

ADMIN_MEDIA_PREFIX = '/static/admin/'

STATICFILES_DIRS = ()
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

SECRET_KEY = 'tmw!okt31h*bc$71u--sp^=)d$0ylz&^&&8g!v(eor(tze9j8#'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'project.urls'

TEMPLATE_DIRS = (
    abspath(join(PROJECT_ROOT, "tempalates"),)
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    # 'django.contrib.staticfiles',
    # 'django.contrib.admin',
    # 'django.contrib.admindocs',

    # Archetype apps
    "archetype",
    "analytical",
    "annoying",
    "compressor",
    "django_extensions",
    "lettuce.django",
    "gunicorn",
    "south",
    "staticfiles",

    # Apps



)

STATICFILES_STORAGE = "staticfiles.storage.CachedStaticFilesStorage"
STATICFILES_EXCLUDED_APPS = []

# See http://docs.djangoproject.com/en/dev/topics/logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
