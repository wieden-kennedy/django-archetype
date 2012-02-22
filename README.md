Welcome to django-archetype.  This project serves as W+K's base django project.  Please use it to get your django project up and running quickly. If you've got improvements or fixes to archetype, send them as a pull request!


Archetype-based project setup
=============================

1. Set up a github repo for your project (aka https://github.com/wieden-kennedy/myproject.git)
1. Clone this repo into your project name, and set up the remotes:
    
    ```bash
    git clone git@github.com:wieden-kennedy/django-archetype.git archetype
    cd archetype
    git remote set-url origin git@github.com:wieden-kennedy/myproject.git
    git push -u origin master
    ```

1. Set up a virtualenv, and re-freeze the requirements

    ```bash
    mkvirtualenv myproject --no-site-packages
    workon myproject
    pip install -r requirements.unstable.txt
    pip freeze requirements.unstable.txt > requirements.txt
    ```
    
    *Note*: If you're in rapid-deploy land, just use requirements.txt. It's guaranteed to be stable.

1. Replace "project" with your project name in the following places:
    * project folder
    * Procfile
    * settings.py, specifically:
        * `ROOT_URLCONF`
        * `DATABASE["NAME"]`
    * fabfile `VIRTUALENV_NAME` and `PROJECT_ROOT`

1.  If you're using AWS (it's set up to, by default):
    * Place your keys into `env/aws_keys.py`.
    * Create whatever buckets you need:

        ```python
        ./manage.py shell_plus

        >>
        from boto.s3.connection import S3Connection
        c = S3Connection(settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY)
        c.create_bucket(settings.AWS_STORAGE_BUCKET_NAME)
        ```

1.  Set the domain in `apps/archetype/fixtures/initial_data.json`
1.  Run `./manage.py test`
1.  Run `./manage.py harvest --settings=envs.lettuce -d`
1.  When both of the above pass, uncomment `"archetype",` in `LETTUCE_AVOID_APPS` in `envs/lettuce.py`
1.  Fill in the settings `ADMINS`.
1.  Update README.md with your project's details.


Setting up Amazon SES to send mail
==================================

1.  Request [production access](http://aws.amazon.com/ses/fullaccessrequest/).
1.  Verify the email address you want to send from.

    ```bash
    ./manage.py shell_plus
    ```

    ```python
    from boto.ses.connection import SESConnection
    c = SESConnection(aws_access_key_id=settings.AWS_ACCESS_KEY_ID, aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)
    c.verify_email_address("outgoingemail@example.com")
    ```

Analytics
=========

Archetype ships with [django-analytical](http://packages.python.org/django-analytical/) built-in.  To add analytics, just add their IDs to the `common.py` settings file.

For instance, to set up Google Analytics and Mixpanel, add:

```python
MIXPANEL_API_TOKEN = "0d123aa10022334455df12345678c"
GOOGLE_ANALYTICS_PROPERTY_ID = "UA-12345678-90"
```

Heroku
======

Setting things up
-----------------

0. Get the heroku gem, if you don't have it.
    
    ```gem install heroku```

1. Create a stack:
    
    ```heroku create --stack cedar my_app```

1. Add the heroku remote
    
    ```git remote add heroku git@heroku.com:my_app.git```

2. Add some typical services:

    ```bash
    # Backups (Free)
    heroku addons:add pgbackups:auto-month

    # A single custom domain (Free)
    heroku addons:add custom_domains:basic
    heroku addons:add zerigo_dns:basic

    # Memcached (5MB, Free)
    heroku addons:add memcache:5mb

    # Set the django env
    heroku config:add DJANGO_ENV="live"

    # Add your domain (You'll need both for www. support.)
    heroku domains:add www.example.com
    heroku domains:add example.com
    ```

3. Set your domain's DNS to zerigo:

    ```
    a.ns.zerigo.net
    b.ns.zerigo.net
    c.ns.zerigo.net
    d.ns.zerigo.net
    e.ns.zerigo.net
    ```

4. Deploy (below)


Deploying
---------

1. Get your `live` branch ready to go.
2. Re-freeeze the requirements, if you've changed them: `pip freeze requirements.unstable.txt > requirements.txt`
3. ```fab deploy_heroku```


Getting a django shell
----------------------

```bash
heroku run python project/manage.py shell_plus
```



Fabric
======

A base set of common fabric commands are included. Right now, that's:

* `deploy_static` - collects static, compresses them, and syncs them to S3.
* `deploy_heroku` - full deploy to heroku. Specifically, it:

    1. Collects all the static files
    1. Combines and compress them
    1. Names them uniquely
    1. Uploads them, gzipped, with never-expire headers to the S3 bucket
    1. Pushes your code to heroku
    1. Runs `syncdb`
    1. Runs `migrate`
    1. Restarts your heroku server
