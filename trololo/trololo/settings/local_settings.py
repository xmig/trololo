EMAIL_HOST_USER = 'jonny.john2017@yandex.ru'
EMAIL_HOST_PASSWORD = 'QueaK1chu3io'
EMAIL_USE_SSL = True
DEFAULT_FROM_EMAIL = 'jonny.john2017@yandex.ru'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'test_db',
#         'USER': 'test_user',
#         'PASSWORD': 'postgres',
#         'HOST': '127.0.0.1',
#         'PORT': '5432',
#     }
# }

SOCIALACCOUNT_PROVIDERS = {
    'github': {
        'METHOD': 'oauth2',
        'SCOPE': ["user"],
    }
}

NOT_INSTALLED_APPS = (
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.linkedin',
    'allauth.socialaccount.providers.google',
)