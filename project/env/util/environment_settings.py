from os import environ


ENVIRONMENT_SETTINGS = [
    "AWS_ACCESS_KEY_ID",
    "AWS_SECRET_ACCESS_KEY",
    "AWS_STORAGE_BUCKET_NAME",
    "DATABASE_PASSWORD",
    "VIRTUALENV_NAME"
]


def _set_from_env_or_fail(setting_name):
    if setting_name in environ:
        globals()[setting_name] = environ[setting_name]


def add_env_settings():
    for s in ENVIRONMENT_SETTINGS:
        _set_from_env_or_fail(s)
