"""
Django settings for the project.

Generated by 'django-admin startproject' using Django 1.10.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# The secret key must be a large random value and it must be kept secret.
try:
    SECRET_KEY = os.environ['SECRET_KEY']
except KeyError:
    raise Exception('Please set the environment variable SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

HIDE_EXPERIMENTAL = os.environ.get('HIDE_EXPERIMENTAL', 'True') == 'True'
HIDE_ALPHA_EXPERIMENTAL = os.environ.get(
    'HIDE_ALPHA_EXPERIMENTAL', 'True') == 'True'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    # Disable Django's own staticfiles handling in favour of WhiteNoise, for
    # greater consistency between gunicorn and `./manage.py runserver`. See:
    # http://whitenoise.evans.io/en/stable/django.html#using-whitenoise-in-development
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_swagger',
    'rest_framework_docs',
    'corsheaders',
    'snippets.apps.SnippetsConfig',
    'experiments.apps.ExperimentsConfig',
    'apiAdmin.apps.ApiAdminConfig',
]

INSTALLED_APPS += (
    # The Django sites framework is required
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # Login via social accounts
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
    # 'allauth.socialaccount.providers.twitter',
    'rest_auth.registration',
    'rest_auth',
)

# following is added to enable registration with email instead of username
AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",

    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = '_main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates/')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = '_main.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
# default to local Postgres database

"""
# How to set the default DB connection
# Add 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
'ENGINE': 'django.db.backends.',
# DB name or path to database file if using sqlite3.
'NAME': '',
# The following settings are not used with sqlite3:
'USER': '',
'PASSWORD': '',
# Empty for localhost through domain sockets or '127.0.0.1' for localhost
# through TCP.
'HOST': '',
'PORT': '',                      # Set to empty string for default.
"""

DATABASES = {
    'default': {
        # default to sqlite3
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Update database configuration with $DATABASE_URL.
# in production, set env variable DATABASE_URL = "postgres://user:password@host:port/database"
# dj_database_url.config(default='postgres://user:password@host:port/database')
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
# http://whitenoise.evans.io/en/stable/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# https://django-rest-swagger.readthedocs.io/en/latest/settings/
SWAGGER_SETTINGS = {
    'USE_SESSION_AUTH': False,
    'SECURITY_DEFINITIONS': {
        # 'basic': {
        #     'type': 'basic'
        # },
        'api_key': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization'
        },
    },
    'SHOW_REQUEST_HEADERS': True,
    'JSON_EDITOR': True,
    'DOC_EXPANSION': None,
    "exclude_namespaces": ["swagger_view"],
    'LOGIN_URL': 'account_login',
    'LOGOUT_URL': 'account_logout',
}

# use allauth UI
# LOGIN_URL = 'rest_framework:login'
# LOGOUT_URL = 'rest_framework:logout'

# http://www.django-rest-framework.org/tutorial/5-relationships-and-hyperlinked-apis/
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        #'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication'
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'PAGE_SIZE': 10,
    # default 'format'; swagger is not working with None
    'URL_FORMAT_OVERRIDE': 'format'
}

API_NAME = os.environ.get('API_NAME', 'My Web API')

# email
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
try:
    EMAIL_HOST = os.environ['EMAIL_HOST']
    EMAIL_PORT = os.environ['EMAIL_PORT']
    EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', False) == 'True'
    EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
    EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
    DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
except KeyError:
    raise Exception('Email service information missing.')
# EMAIL_BACKEND = "sgbackend.SendGridBackend"
# SENDGRID_API_KEY = os.environ['SENDGRID_API_KEY']

SITE_ID = 1

REST_USE_JWT = False
REST_SESSION_LOGIN = False

# ”username” | “email” | “username_email”
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'optional'  # 'mandatory'
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_REQUIRED = True   # must be True if 'email' authentication is used
ACCOUNT_USERNAME_REQUIRED = False
LOGIN_REDIRECT_URL = '/'

SOCIALACCOUNT_EMAIL_VERIFICATION = "none"
SOCIALACCOUNT_EMAIL_REQUIRED = True
SOCIALACCOUNT_QUERY_EMAIL = True

# output settings to console
if DEBUG:
    print('BASE_DIR: ' + BASE_DIR)
    print('PROJECT_ROOT : ' + PROJECT_ROOT)
    print('SECRET_KEY: ' + SECRET_KEY)
    print('DEBUG: ' + str(DEBUG))
    print('HIDE_EXPERIMENTAL: ' + str(HIDE_EXPERIMENTAL))
    print('HIDE_ALPHA_EXPERIMENTAL: ' + str(HIDE_ALPHA_EXPERIMENTAL))
    print('Database Engine: ' + DATABASES['default']['ENGINE'])
    print('EMAIL_HOST: ' + EMAIL_HOST)
    print('EMAIL_PORT: ' + EMAIL_PORT)
    print('EMAIL_USE_TLS: ' + str(EMAIL_USE_TLS))
    print('EMAIL_HOST_USER: ' + EMAIL_HOST_USER)
    print('EMAIL_HOST_PASSWORD: ' + EMAIL_HOST_PASSWORD)
