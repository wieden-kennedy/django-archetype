from envs.common import *
import os

DEBUG = False
TEMPLATE_DEBUG = DEBUG


DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

if not "AWS_ACCESS_KEY_ID" in locals():
    AWS_ACCESS_KEY_ID = os.environ["AWS_ACCESS_KEY_ID"]

if not "AWS_SECRET_ACCESS_KEY" in locals():
    AWS_SECRET_ACCESS_KEY = os.environ["AWS_SECRET_ACCESS_KEY"]

if not "AWS_STORAGE_BUCKET_NAME" in locals():
    AWS_STORAGE_BUCKET_NAME = os.environ["AWS_STORAGE_BUCKET_NAME"]


STATIC_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
