import json
import random
import os
from functools import wraps
from PIL import Image, ImageDraw, ImageFont
from django.core.cache import caches

MAX_THUMBNAIL_SIZE = 112.0
color_choices = ['green', 'black', 'orange', 'pink', 'blue', 'purple']


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


def generate_image(text, path_to_file):
    img_size = int(MAX_THUMBNAIL_SIZE)

    img = Image.new("RGB", (img_size, img_size), random.choice(color_choices))
    # font URL: http://www.fonts2u.com/enigmatic-unicode-regular.font
    font_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'EnigmaU_2.TTF'))
    font = ImageFont.truetype(font_path, 90, encoding="unic")
    draw = ImageDraw.Draw(img)

    w, h = draw.textsize(text, font=font)
    draw.text(((img_size - w) / 2, (img_size - h) / 2), text, font=font, fill="white")
    img.save(path_to_file, "JPEG")


def resize_logo(instance):
    """
    Resize model logo to needed sizes.
    """
    width = instance.photo.width
    height = instance.photo.height

    filename = instance.photo.path
    max_size = max(width, height)

    if max_size > MAX_THUMBNAIL_SIZE:
        ratio = min(MAX_THUMBNAIL_SIZE/width, MAX_THUMBNAIL_SIZE/height)
        image = Image.open(filename)
        image = image.resize(
            (int(round(width * ratio)), int(round(height * ratio))),
            Image.ANTIALIAS
        )
        image.save(filename)