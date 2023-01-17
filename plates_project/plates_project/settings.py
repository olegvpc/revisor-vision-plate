"""
Django settings for plates_project project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path

from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-m+1vhvj7f$ia1=9hq4@d8ttvstq=$s==^%gsp86l^4j%1!l&3u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'drf_yasg',
    'rest_framework',
    'djoser',
    'corsheaders',
    'plates.apps.PlatesConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'plates_project.urls'

TEMPLATES_DIR = BASE_DIR / 'templates'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
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

WSGI_APPLICATION = 'plates_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': os.environ.get('DB_ENGINE', default='django.db.backends.postgresql'),
            'NAME': os.environ.get('DB_NAME', default='postgres'),
            'USER': os.environ.get('POSTGRES_USER', default='postgres'),
            'PASSWORD': os.environ.get('POSTGRES_PASSWORD', default='postgres'),
            'HOST': os.environ.get('DB_HOST', default='db'),
            'PORT': os.environ.get('DB_PORT', default='5432'),
        }
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# JSON Web Token
# можно СОЗДАВАТЬ новых пользователей через
# POST запрос на http://127.0.0.1:8000/auth/users/
# {
#     "username": "oleg-1",
#     "password": "12345poiuy"
# }
# ответ {
#     "email": "",
#     "username": "oleg-1",
#     "id": 2
# }

# далее получаем новый Token - Bearer для пользователя
# по POST запросу
# http://127.0.0.1:8000/auth/jwt/create/
# в виде
# {
#     "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1ODQ3NjU2NiwianRpIjoiYzFmNTY4MjQ3M2Q4NGE4MzlhZWZmYTdmMzQ0MzExZTIiLCJ1c2VyX2lkIjo0fQ.U7fP2I-jyGzTojrZ8Y4ZHWjDDVMMYwCs-ga5h2ObXrk",
#     "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY3MDMwMTY2LCJqdGkiOiIwODU3OTQ5OWYwZWI0MmY5YWE1OGNhMTQzZjhmOTZmYyIsInVzZXJfaWQiOjR9.Y9q6nSEh7ihe-IeLbEvPSG6xLZx9RQrdOwPFC32EThk"
# }
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],

    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}
#

SIMPLE_JWT = {
    # Устанавливаем срок жизни токена
   'ACCESS_TOKEN_LIFETIME': timedelta(days=100),
   'AUTH_HEADER_TYPES': ('Bearer',),
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static/'),)
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ORIGIN_ALLOW_ALL = True

