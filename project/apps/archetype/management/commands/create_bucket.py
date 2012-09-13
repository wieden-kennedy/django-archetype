from django.core.management.base import BaseCommand
from django.conf import settings
from boto.s3.connection import S3Connection
from boto.s3.cors import CORSConfiguration


class Command(BaseCommand):

    def handle(self, *args, **options):
        c = S3Connection(settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY)
        bucket = c.lookup(settings.AWS_STORAGE_BUCKET_NAME)
        if not bucket:
            bucket = c.create_bucket(settings.AWS_STORAGE_BUCKET_NAME)

        cors_cfg = CORSConfiguration()
        cors_cfg.add_rule('GET', '*')
        bucket.set_cors(cors_cfg)
