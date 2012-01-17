Welcome to django-archetype.  This project serves as W+K's base django project.  Please fork it, and use it to get your django project up and running quickly. If you've got improvements or fixes to archetype, send them as a pull request!


Archetype-based project setup
=============================

1. Fork this repo
1. Clone down your forked repo
1. Set up a virtualenv, and `pip install -r requirements.txt`
1. Replace "project" with your project name in the following places:
    * project folder
    * Procfile
    * settings.py, specifically:
        * `ROOT_URLCONF`
        * `DATABASE["NAME"]`

1.  If you're using AWS (it's set up to, by default), place your keys into `env/aws_keys.py`.
1.  Set the domain in `apps/archetype/fixtures/initial_data.json`
1.  Run `./manage.py test`
1.  Run `./manage.py harvest --settings=envs.lettuce -d`
1.  If both of the above pass, you should remove the `archetype_test` entry in urls.py


Deploying to Heroku
===================

To set up heroku for deploy, you'll need to add this key:

```
heroku config:add DJANGO_ENV="live"
```

To deploy:

```
./manage.py collectstatic --noinput
./manage.py compress  --force
./manage.py sync_static_s3 --gzip --expires
git push heroku live:master
heroku run project/manage.py syncdb
heroku run project/manage.py migrate
heroku restart
```
