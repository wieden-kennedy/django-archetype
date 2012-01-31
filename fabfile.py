from fabric.api import *
from os.path import abspath, dirname, join

env.VIRTUALENV_ROOT = "~/.virtualenvs"

env.VIRTUALENV_NAME = "myproject"
env.PROJECT_ROOT = abspath(join(dirname(__file__), "project"))
env.SETTINGS = "envs.live"


def _local_in_virtualenv(cmd):
    env.cmd = cmd
    local("source %(VIRTUALENV_ROOT)s/%(VIRTUALENV_NAME)s/bin/activate;cd %(PROJECT_ROOT)s;%(cmd)s" % env)


def deploy_static():
    _local_in_virtualenv("./manage.py collectstatic --noinput --settings=%(SETTINGS)s" % env)
    _local_in_virtualenv("./manage.py compress --force --settings=%(SETTINGS)s" % env)
    _local_in_virtualenv("./manage.py sync_static_s3 --gzip --expires --settings=%(SETTINGS)s" % env)
