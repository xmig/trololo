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

# SERVER_PORT = 8000
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

INSTALLED_APPS += (
    'rest_framework_swagger',
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SWAGGER_SETTINGS = {
    'exclude_namespaces': [],
    'api_version': '0.1',
    'api_path': '/',
    'enabled_methods': [
        'get',
        'post',
        'put',
        'patch',
        'delete'
    ],
    'api_key': '',
    'is_authenticated': False,
    'is_superuser': False,
    'unauthenticated_user': 'django.contrib.auth.models.AnonymousUser',
    'permission_denied_handler': None,
    'resource_access_handler': None,
    'base_path':'127.0.0.1:8000/docs',
    'info': {
        'contact': '',
        'description': '',
        'license': '',
        'licenseUrl': '',
        'termsOfServiceUrl': '',
        'title': 'Trololo API',
    },
    'doc_expansion': 'none',
}

SITE_ID = 2

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'trololo',
        'USER': 'trololo',
        'PASSWORD': 'trololo',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}