from django.core.management.base import BaseCommand
from django.conf import settings
from boto.s3.connection import S3Connection

class Command(BaseCommand):

    def handle(self, *args, **options):
        c = S3Connection(settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY)
        c.create_bucket(settings.AWS_STORAGE_BUCKET_NAME)