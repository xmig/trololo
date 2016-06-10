"""
Django settings for trololo project.
"""

import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'jsa)6+4tm14a==zehmcjqnyr&qjy!b1ka#fd3@zw5uc43ees9c'
ALLOWED_HOSTS = []

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'allauth',
    'allauth.account',
    'rest_auth.registration',
    'taggit',
    'users',
    'cuser',
    'chi_django_base',
    'activity',
    'projects.projects_app.ProjectsAppConfig',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.linkedin',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.google',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'cuser.middleware.CuserMiddleware',
)

ROOT_URLCONF = 'trololo.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.abspath(os.path.join(BASE_DIR, os.pardir, 'app'))
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.request',
                'django.template.context_processors.i18n',
            ],
        },
    },
]

WSGI_APPLICATION = 'trololo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
MEDIA_URL = '/media/'
MEDIA_ROOT = '/var/www/trololo/media'

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

LANGUAGES = (
    ('ru', 'Russian'),
    ('en', 'English'),
)

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.abspath(os.path.join(BASE_DIR, os.path.pardir, 'app', 'static')),
    os.path.abspath(os.path.join(BASE_DIR, os.path.pardir, 'app', 'partials')),
]

LOGIN_URL = '/'


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES' : (
        'rest_framework.permissions.IsAuthenticated',
    ),
    # 'PAGE_SIZE': 10,
    'DEFAULT_PAGINATION_CLASS': 'chi_django_base.paginators.StandardResultsSetPagination',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication'
    )
}

AUTH_USER_MODEL = 'users.TrololoUser'
ACTIVITY_MODEL = 'activity.Activity'
STATUS_MODEL = 'projects.Status'
# option for registration
SITE_ID = 1

# email settings
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465

# authorization settings
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
# ACCOUNT_AUTHENTICATION_METHOD = "username_email"

AUTHENTICATION_BACKENDS = [
    'chi_django_base.auth_backends.EmailAuthBackend',
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

# social auth config
SOCIALACCOUNT_PROVIDERS = {
    'facebook':
       {'METHOD': 'oauth2',
        'SCOPE': ['email', 'public_profile', 'user_friends'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'FIELDS': [
            'id',
            'email',
            'name',
            'first_name',
            'last_name',
            'verified',
            'locale',
            'timezone',
            'link',
            'gender',
            'updated_time'],
        'EXCHANGE_TOKEN': True,
        # 'LOCALE_FUNC': 'path.to.callable',
        'VERIFIED_EMAIL': False,
        'VERSION': 'v2.5'},
    'linkedin':
        {'SCOPE': ['r_emailaddress'],
         'PROFILE_FIELDS': ['id',
                         'first-name',
                         'last-name',
                         'email-address',
                         'picture-url',
                         'public-profile-url']},
    'github': {
        'METHOD': 'oauth2',
        'SCOPE': ["user"],
    },
    'google': {
        'SCOPE': ['profile', 'email'],
        'AUTH_PARAMS': { 'access_type': 'online' }
    }
}

SOCIALACCOUNT_EMAIL_VERIFICATION = False

# caching config
REST_FRAMEWORK_EXTENSIONS = {
    'DEFAULT_CACHE_ERRORS': False,
    'DEFAULT_CACHE_KEY_FUNC': 'chi_django_base.helpers.calculate_cache_key',
    'DEFAULT_CACHE_RESPONSE_TIMEOUT': 60 * 15  # 15 minutes
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

###################
## SPHINX CONFIG ##
###################

# deprecated
GLOBAL_SEARCH_URL = 'http://127.0.0.1:8005/find/'

# from sphinxapi
# http://sphinxsearch.com/docs/current.html#extended-syntax
SPHINX_MATCH_MODE = 2  # SPH_MATCH_EXTENDED2

SPHINX_SEARCH_PARAMS = {
    'mode':     SPHINX_MATCH_MODE,
    'host':     'localhost',
    'port':     10312,
    'index':    '*',
    'weights':  [10, 1],
}

# enable sending of activity email notifications
SEND_EMAIL_NOTIFICATION = True

# celery config
BROKER_URL = 'redis://'
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT=['json']
CELERY_TIMEZONE = 'Europe/Kiev'
CELERY_ENABLE_UTC = True
