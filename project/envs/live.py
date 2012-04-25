from envs.common import *
import os

DEBUG = False
TEMPLATE_DEBUG = DEBUG

EMAIL_BACKEND = 'django_ses.SESBackend'

if not "AWS_ACCESS_KEY_ID" in locals():
    AWS_ACCESS_KEY_ID = os.environ["AWS_ACCESS_KEY_ID"]

if not "AWS_SECRET_ACCESS_KEY" in locals():
    AWS_SECRET_ACCESS_KEY = os.environ["AWS_SECRET_ACCESS_KEY"]

if not "AWS_STORAGE_BUCKET_NAME" in locals():
    AWS_STORAGE_BUCKET_NAME = os.environ["AWS_STORAGE_BUCKET_NAME"]


STATIC_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
MEDIA_URL = '%smedia/' % STATIC_URL

ADMIN_MEDIA_PREFIX = "%sadmin/" % STATIC_URL
COMPRESS_URL = STATIC_URL
FAVICON_URL = "%sfavicon.ico" % STATIC_URL

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE = "archetype.custom_storages.CachedS3BotoStorage"
COMPRESS_STORAGE = STATICFILES_STORAGE
COMPRESS_OFFLINE = True
COMPRESS_ENABLED = True

# Heroku Memcache addon
# CACHES = {
#     'default': {
#         'BACKEND': 'django_pylibmc.memcached.PyLibMCCache'
#     }
# }

# Heroku Redis for cache and celery config
# try:
#     if 'REDISTOGO_URL' in os.environ:
#         import urlparse
#         urlparse.uses_netloc.append('redis')
#         url = urlparse.urlparse(os.environ['REDISTOGO_URL'])

#         CACHES = {
#             'default': {
#                 'BACKEND': 'redis_cache.RedisCache',
#                 'LOCATION': '%s:%s' % (url.hostname, url.port),
#                 'OPTIONS': {
#                     'DB': 0,
#                     'PASSWORD': url.password,
#                     'PARSER_CLASS': 'redis.connection.HiredisParser'
#                 },
#             },
#         }
#         CELERY_REDIS_HOST = url.hostname
#         CELERY_REDIS_PORT = url.port
#         CELERY_REDIS_DB = 0
#         CELERY_REDIS_PASSWORD = url.password
#         BROKER_URL = "redis://redistogo:%s@%s:%s/0" % (url.password, url.hostname, url.port)
# except:
#     pass
