import json
from functools import wraps
from django.core.cache import caches


def calculate_cache_key(view_instance, view_method, request, args, kwargs):
    key = '::'.join([
        view_instance.__class__.__name__,
        view_method.__name__,
        request.path,
        request.META['HTTP_ACCEPT'],
        json.dumps(dict(request.query_params)),
        request.user.username
    ])

    return key


def remove_cache_key(key_prefix, cache):
    keys = cache.keys("*{0}*".format(key_prefix))
    for key in keys:
        cache.delete(key)


def invalidate_cache(cache_keys_prefixes):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            resp = func(*args, **kwargs)

            if 199 < resp.status_code < 300:
                for prefix in cache_keys_prefixes:
                    remove_cache_key(prefix, caches['default'])

            return resp

        return wrapper

    return decorator