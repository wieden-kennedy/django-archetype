from os.path import abspath, join, dirname
from sys import path
from util import environment_settings
globals().update(environment_settings.env_settings())


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

DEFAULT_FROM_EMAIL = "robot@wk.com"
SERVER_EMAIL = DEFAULT_FROM_EMAIL
EMAIL_SUBJECT_PREFIX = "[ProjectName]"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'project.sqlite3',            # Or path to database file if using sqlite3.
        'USER': '',                       # Not used with sqlite3.
        'PASSWORD': '',                   # Not used with sqlite3.
        'HOST': '',                       # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                       # Set to empty string for default. Not used with sqlite3.
    }
}

# BROKER_URL = "redis://localhost:6379/0"
# CELERY_REDIS_HOST = "127.0.0.1"
# CELERY_REDIS_PORT = 6379
# CELERY_REDIS_DB = 0
# CELERY_REDIS_PASSWORD = None


TIME_ZONE = 'America/Vancouver'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = False
USE_L10N = False


MEDIA_ROOT = join(PROJECT_ROOT, "media_root")
MEDIA_URL = '/media/'

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
    # 'subdomains.middleware.SubdomainURLRoutingMiddleware',  # Need subdomain routing? Use this!
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
)

ROOT_URLCONF = 'project.urls'

TEMPLATE_DIRS = (
    abspath(join(PROJECT_ROOT, "templates"),)
)

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

    # Apps
    # "autoscalebot",


]

# Analytics
INTERNAL_IPS = ["localhost", "127.0.0.1", "0.0.0.0"]
# MIXPANEL_API_TOKEN = ""
# GOOGLE_ANALYTICS_PROPERTY_ID = ""
# GAUGES_SITE_ID = ""

# AUTH_PROFILE_MODULE = 'people.Person'

STATICFILES_EXCLUDED_APPS = []
COMPRESS_ROOT = STATIC_ROOT

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

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

SOUTH_TESTS_MIGRATE = True

AUTOSCALE_HEROKU_APP_NAME = "project"
AUTOSCALE_HEROKU_API_KEY = "key"
AUTOSCALE_HEARTBEAT_INTERVAL_IN_SECONDS = 5
AUTOSCALE_HEARTBEAT_URL = 'http://www.example.com/heartbeat'
AUTOSCALE_MAX_RESPONSE_TIME_IN_MS = 1500
AUTOSCALE_MIN_RESPONSE_TIME_IN_MS = 400
AUTOSCALE_NUMBER_OF_FAILS_TO_SCALE_UP_AFTER = 4
AUTOSCALE_NUMBER_OF_PASSES_TO_SCALE_DOWN_AFTER = 6
AUTOSCALE_MAX_DYNOS = 5
AUTOSCALE_MIN_DYNOS = 1
AUTOSCALE_INCREMENT = 1
AUTOSCALE_NOTIFY_IF_SCALE_DIFF_EXCEEDS_THRESHOLD = None
AUTOSCALE_NOTIFY_IF_SCALE_DIFF_EXCEEDS_PERIOD_IN_MINUTES = None
AUTOSCALE_NOTIFY_IF_NEEDS_EXCEED_MAX = True
AUTOSCALE_NOTIFY_IF_NEEDS_BELOW_MIN = True
AUTOSCALE_NOTIFY_ON_EVERY_PING = False
AUTOSCALE_NOTIFICATION_BACKENDS = [
    'autoscalebot.backends.notification.DjangoEmailBackend',
    'autoscalebot.backends.notification.ConsoleBackend',
]
