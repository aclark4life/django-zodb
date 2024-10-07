"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 5.0.9.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-19d29*-+)oj5mnwy=1rjy#8l^pw2y9ljf@vty48ns*pg%52$k2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

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

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django_zodb',
        'NAME': 'mydb',
        'HOST': 'localhost',  # ZEO server host
        'PORT': 8100,  # ZEO server port
        'OPTIONS': {
	    'FILE_STORAGE': 'Data.fs',  # File storage path
            'BLOB_STORAGE': 'blobstorage',  # Blob storage directory
            # Additional ZEO/ZODB-specific options can be added here
        },
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
INSTALLED_APPS.append("search")  # noqa
# django-zodb
#
# Uncomment next two lines to enable custom admin
# INSTALLED_APPS = [app for app in INSTALLED_APPS if app != 'django.contrib.admin']
# INSTALLED_APPS.append('backend.apps.CustomAdminConfig')
import os  # noqa
import dj_database_url  # noqa

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
EXPLORER_CONNECTIONS = {"Default": "default"}
EXPLORER_DEFAULT_CONNECTION = "default"
LOGIN_REDIRECT_URL = "/"
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SILENCED_SYSTEM_CHECKS = ["django_recaptcha.recaptcha_test_key_error"]
BASE_DIR = os.path.dirname(PROJECT_DIR)
STATICFILES_DIRS = []
WEBPACK_LOADER = {
    "MANIFEST_FILE": os.path.join(BASE_DIR, "frontend/build/manifest.json"),
}
STATICFILES_DIRS.append(os.path.join(BASE_DIR, "frontend/build"))
TEMPLATES[0]["DIRS"].append(os.path.join(PROJECT_DIR, "templates"))
THEMES = [
    ("light", "Light Theme"),
    ("dark", "Dark Theme"),
]
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly"
    ]
}
INSTALLED_APPS.append("allauth")
INSTALLED_APPS.append("allauth.account")
INSTALLED_APPS.append("allauth.socialaccount")
INSTALLED_APPS.append("crispy_bootstrap5")
INSTALLED_APPS.append("crispy_forms")
INSTALLED_APPS.append("debug_toolbar")
INSTALLED_APPS.append("django_extensions")
INSTALLED_APPS.append("django_recaptcha")
INSTALLED_APPS.append("rest_framework")
INSTALLED_APPS.append("rest_framework.authtoken")
INSTALLED_APPS.append("webpack_boilerplate")
INSTALLED_APPS.append("explorer")
MIDDLEWARE.append("allauth.account.middleware.AccountMiddleware")
CRISPY_TEMPLATE_PACK = "bootstrap5"
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
