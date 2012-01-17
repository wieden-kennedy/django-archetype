from envs.dev import *

# Dev specific stuff
SITE_ID = 2

SOUTH_TESTS_MIGRATE = True

# Use mysql, for actually relevant results
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'salad_test_project.sqlite3',
        'USER': 'root',
        'PASSWORD': '',
    }
}

LETTUCE_AVOID_APPS = (
    "analytical",
    "annoying",
    "compressor",
    "django_extensions",
    "gunicorn",
    "south",
    "staticfiles",
)

LETTUCE_PORT = 8000
