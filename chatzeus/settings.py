"""
Django settings for chatzeus project.

Generated by 'django-admin startproject' using Django 3.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
import environ
import boto3

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Configure environment
env = environ.Env()
env.read_env(os.path.join(BASE_DIR, '.env'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')


# Application definition

INSTALLED_APPS = [
    'chat.apps.ChatConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "corsheaders",
    'rest_framework',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOWED_ORIGINS = env.list('CORS_ALLOWED_ORIGINS')

ROOT_URLCONF = 'chatzeus.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'chatzeus.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': env.db(),
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#collectstatic先のディレクトリ
STATIC_ROOT = env('STATIC_ROOT')
MEDIA_ROOT = env('MEDIA_ROOT')

# Logginの設定（CloudWatchに出力）
AWS_REGION_NAME = "ap-northeast-1"

boto3_logs_client = boto3.client("logs", region_name=AWS_REGION_NAME)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'root': {
        'level': 'DEBUG',
        # Adding the watchtower handler here causes all loggers in the project that
        # have propagate=True (the default) to send messages to watchtower. If you
        # wish to send only from specific loggers instead, remove "watchtower" here
        # and configure individual loggers below.
        'handlers': ['watchtower', 'console'],
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
        'watchtower': {
            'class': 'watchtower.CloudWatchLogHandler',
            'boto3_client': boto3_logs_client,
            'log_group_name': 'chatzeus',
            # Decrease the verbosity level here to send only those logs to watchtower,
            # but still see more verbose logs in the console. See the watchtower
            # documentation for other parameters that can be set here.
            'level': 'DEBUG'
        }
    },
    'loggers': {
        # In the debug server (`manage.py runserver`), several Django system loggers cause
        # deadlocks when using threading in the logging handler, and are not supported by
        # watchtower. This limitation does not apply when running on production WSGI servers
        # (gunicorn, uwsgi, etc.), so we recommend that you set `propagate=True` below in your
        # production-specific Django settings file to receive Django system logs in CloudWatch.
        'django': {
            'level': 'INFO',
            'handlers': ['console'],
            'propagate': False
        },
        # Add any other logger-specific configuration here.
        'chat': {
            'level': 'INFO',
            'handlers': ['console'],
            'propagate': False
        }
    }
}