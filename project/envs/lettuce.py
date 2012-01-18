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

# Necessary to match the magic that lettuce does in serving static media.
NEW_STATICFILES_FINDERS = ()
for f in STATICFILES_FINDERS:
    if f == 'staticfiles.finders.FileSystemFinder':
        NEW_STATICFILES_FINDERS += ('django.contrib.staticfiles.finders.FileSystemFinder',)
    elif f == 'staticfiles.finders.AppDirectoriesFinder':
        NEW_STATICFILES_FINDERS += ('django.contrib.staticfiles.finders.AppDirectoriesFinder',)
    else:
        NEW_STATICFILES_FINDERS += (f,)

STATICFILES_FINDERS = NEW_STATICFILES_FINDERS


LETTUCE_PORT = 8000
