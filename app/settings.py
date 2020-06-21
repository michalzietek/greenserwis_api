try:
    from app.local_settings import * # NOQA
except ImportError:

    raise Exception(
        'ImportError local_settings, use local_settings.py.template')
