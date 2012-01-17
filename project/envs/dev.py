from envs.common import *

# Dev specific stuff
SITE_ID = 2

COMPRESS_OFFLINE = True
COMPRESS_OFFLINE_CONTEXT = {
    'STATIC_URL': STATIC_URL,
    'MEDIA_URL': MEDIA_URL,
}
