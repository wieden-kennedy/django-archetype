"""
Download cache manifest from the CDN
====================================

Compressor generates a manifest.json file that holds all of the
static filename mappings. Unfortunately, because heroku is read-only,
and because compressor generates this file when we're ready to deploy,
it would require an additional git commit to pass it with the source.

./manage.py download_manifest

Solves this, by grabbing the manifest.json from the CDN, and placing it
into the COMPRESS_ROOT.

"""
import optparse
from os import makedirs
from os.path import abspath, join, exists
import urllib2

from django.core.management.base import BaseCommand
CACHE_FILE_DIR = "CACHE"
CACHE_FILE_NAME = "manifest.json"


class Command(BaseCommand):

    help = 'Grabs the manifest.json from STATIC_URL, and saves it to COMPRESS_URL.'

    option_list = BaseCommand.option_list + (
        optparse.make_option('--force',
            action='store_true', dest='force', default=False,
            help="Download the manifest even if it already exists."),
    )
    can_import_settings = True

    def handle(self, *args, **options):
        from django.conf import settings

        # If we already have a manifest:
        manifest_dir = abspath(join(settings.STATIC_ROOT, CACHE_FILE_DIR))
        manifest_file_path = abspath(join(settings.STATIC_ROOT, CACHE_FILE_DIR, CACHE_FILE_NAME))
        if not exists(manifest_file_path) or options.get('force'):
            response = urllib2.urlopen('%s%s/%s' % (settings.STATIC_URL, CACHE_FILE_DIR, CACHE_FILE_NAME))
            manifest_content = response.read()
            makedirs(manifest_dir)

            manifest_file = open(manifest_file_path, "w+")
            manifest_file.write(manifest_content)
            manifest_file.close()
