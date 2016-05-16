from .base import *

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
# LOGGING
# See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
from logging import Filter


class FilterDBLogs(Filter):
    def filter(self, record):
        skip_records = [
            "ALTER SEQUENCE", "CREATE TABLE",
            "CREATE INDEX", "ALTER TABLE",
        ]

        for r in skip_records:
            if record.msg.startswith(r):
                return 0

        return 1


LOGGING = {
    'version': 1,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s',
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s [%(name)s %(asctime)s] %(message)s'
        }
    },
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'db_query_filter': {
            '()': 'trololo.settings.development.FilterDBLogs'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'db_log': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
            'filters': ['db_query_filter'],
        }
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
        # 'django.db.backends': {
        #     'handlers': ['db_log'],
        #     'level': 'DEBUG',
        #     'propagate': False
        # },
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
    'base_path':'localhost:8000/docs',
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

SITE_ID = 4

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'test_db',
        'USER': 'test_user',
        'PASSWORD': 'test',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# for test speed up
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher'
]

USE_GLOBAL_SEARCH = False
PROJECT_INDEX = 'project_rt'
TASK_INDEX = 'task_rt'
TASK_COMMENT_INDEX = 'task_comment_rt'

SPHINX_INDEXES = [PROJECT_INDEX, TASK_INDEX, TASK_COMMENT_INDEX]

try:
    from local_settings import *
except ImportError:
    pass

if 'NOT_INSTALLED_APPS' in locals():
    INSTALLED_APPS = tuple(
        set(INSTALLED_APPS) - set(NOT_INSTALLED_APPS)
    )