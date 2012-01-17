import os

if 'DJANGO_ENV' in os.environ and os.environ["DJANGO_ENV"] == "live":
    from envs.live import *
else:
    from envs.dev import *
