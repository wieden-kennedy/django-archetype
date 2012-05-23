from fabric.api import *
from project.env import local as local_settings
from os.path import abspath, dirname, join

env.VIRTUALENV_ROOT = "~/.virtualenvs"
env.VIRTUALENV_NAME = local_settings.VIRTUALENV_NAME
env.PROJECT_NAME = "project"
env.SETTINGS = "env.live"

env.PROJECT_ROOT = abspath(join(dirname(__file__), env.PROJECT_NAME))


def _local_in_virtualenv(cmd):
    env.cmd = cmd
    local("source %(VIRTUALENV_ROOT)s/%(VIRTUALENV_NAME)s/bin/activate;cd %(PROJECT_ROOT)s;%(cmd)s" % env)


def create_bucket():
    _local_in_virtualenv("./manage.py create_bucket --settings=%(SETTINGS)s" % env)


def deploy_static():
    _local_in_virtualenv("./manage.py collectstatic --noinput --settings=%(SETTINGS)s" % env)
    _local_in_virtualenv("./manage.py compress --force --settings=%(SETTINGS)s" % env)
    _local_in_virtualenv("./manage.py sync_static_s3 --gzip --expires --settings=%(SETTINGS)s" % env)


def deploy_heroku(branch_name="live", heroku_remote="heroku"):
    deploy_static()
    _local_in_virtualenv("git push %s %s:master" % (heroku_remote, branch_name))
    _local_in_virtualenv("heroku run %(PROJECT_NAME)s/manage.py syncdb" % env)
    _local_in_virtualenv("heroku run %(PROJECT_NAME)s/manage.py migrate" % env)
    _local_in_virtualenv("heroku restart")
