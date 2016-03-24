from .base import *

MEDIA_ROOT = '/var/www/trololo/media/prod/'
STATIC_ROOT = '/var/www/trololo/static/prod/'

ALLOWED_HOSTS = ['127.0.0.1', 'worddict.net']

# LOGGING
# See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
LOGGING = {
    'version': 1,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s',
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        }
    },
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
            },
        'file': {
            'level': 'INFO',
            #'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/home/ubuntu/projects/trololo/logs/prod_app.log',
            'maxBytes': 1024 * 1024 * 10, # 10 MB
            'backupCount': 2,
            'formatter': 'verbose'
            }
        },
    'loggers': {
        'django.request': {
            'handlers': ['file'],
            'level': 'WARNING',
            'propagate': True,
        },
        'django': {
            'handlers': ['file'],
            'level': 'WARNING',
            'propagate': True,
        },
        'app': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'trololo_prod',
        'USER': 'trololo_user',
        'PASSWORD': 'louShoote6',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}