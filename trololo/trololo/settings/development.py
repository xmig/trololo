from .base import *

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
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
        # 'file': {
        #     #'level': 'INFO',
        #     'level': 'DEBUG',
        #     'class': 'logging.handlers.RotatingFileHandler',
        #     'filename': 'app.log',
        #     'maxBytes': 1024*1024*50, # 50 MB
        #     'backupCount': 10,
        #     'formatter': 'verbose'
        #     }
        },
    'loggers': {
        'django.request': {
            'handlers': ['console'],
            'level': 'WARNING',
            'propagate': True,
        },
        'django': {
            'handlers': ['console'],
            'level': 'WARNING',
            'propagate': True,
        },
        'app': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}