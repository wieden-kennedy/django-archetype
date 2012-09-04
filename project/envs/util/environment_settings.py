from os import environ


ENVIRONMENT_SETTINGS = [
    "AWS_ACCESS_KEY_ID",
    "AWS_SECRET_ACCESS_KEY",
    "AWS_STORAGE_BUCKET_NAME",
    "DATABASE_PASSWORD",
    "VIRTUALENV_NAME",
]


def env_settings():
    d = {}
    for s in ENVIRONMENT_SETTINGS:
        if s in environ:
            d[s] = environ[s]
    return d
