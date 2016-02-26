"""
Gravatar - this image that follows you from site to site
appearing when you send a comment or write a blog
"""
import urllib, hashlib


def get_avatavr_url(email, default="http://www.example.com/default.jpg", size=50):
    """
    :param email: e-mail user
    :param default: the default URL
    :param size: image size in pixels
    :return: returns a reference to the picture URL
    """
    gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest() + "?"
    gravatar_url += urllib.urlencode({'d':default, 's':str(size)})
    return gravatar_url
