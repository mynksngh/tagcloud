from django.conf import settings


def read_setting(name, default=None):
    if hasattr(settings, name):
        return getattr(settings, name)
    else:
        return default
