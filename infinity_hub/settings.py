"""
Django settings for infinity_hub project.

Generated by 'django-admin startproject' using Django 4.2.11.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
import dj_database_url

if os.path.isfile("env.py"):
    import env


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# DMcC 25/04/24 Message storage in session
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

X_FRAME_OPTIONS = 'ALLOW-FROM https://amiresponsive.co.uk/ https://responsivedesignchecker.com/ https://techsini.com/multi-mockup/'

ALLOWED_HOSTS = ['infinity-hub-15161149b9fb.herokuapp.com',
                 '8000-vasileios20-infinityhub-tnlazceugrf.ws-eu110.gitpod.io',
                 '8000-vasileios20-infinityhub-n7uovthffb0.ws-eu110.gitpod.io',
                 'https://8000-vasileios20-infinityhub-tnlazceugrf.ws-eu110.gitpod.io',
                 '8000-vasileios20-infinityhub-qu8k940y57n.ws-eu110.gitpod.io',
                 '8000-vasileios20-infinityhub-n1cualn8mni.ws-eu110.gitpod.io',
                 '8000-vasileios20-infinityhub-qyq3ge7a31m.ws-eu110.gitpod.io',
                 '8000-vasileios20-infinityhub-4htg50os38c.ws-eu110.gitpod.io',
                 '8000-vasileios20-infinityhub-xk4h0mfxmiw.ws-eu110.gitpod.io',
                 'localhost', '8000-vasileios20-infinityhub-8ln40mftbwt.ws-eu110.gitpod.io', '127.0.0.1']

CSRF_TRUSTED_ORIGINS = [
    ('https://8000-vasileios20-infinityhub-tnlazceugrf.'
     + 'ws-eu110.gitpod.io'),
    'https://8000-vasileios20-infinityhub-n7uovthffb0.ws-eu110.gitpod.io',
    'https://8000-vasileios20-infinityhub-n1cualn8mni.ws-eu110.gitpod.io',
    'https://8000-vasileios20-infinityhub-qyq3ge7a31m.ws-eu110.gitpod.io',
    'https://8000-vasileios20-infinityhub-4htg50os38c.ws-eu110.gitpod.io',
    'https://8000-vasileios20-infinityhub-xk4h0mfxmiw.ws-eu110.gitpod.io',
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'django.contrib.staticfiles',
    'cloudinary_storage',
    'cloudinary',
    'crispy_forms',
    'crispy_bootstrap4',
    'home',
    'contact',
    'forum',
    'profiles',
    'django_summernote',
]

SITE_ID = 1

X_FRAME_OPTIONS = 'SAMEORIGIN'

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

APPEND_SLASH = False

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'infinity_hub.urls'

# DMcC Removed account email verification as throwing a ports error
ACCOUNT_EMAIL_VERIFICATION = 'none'

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

WSGI_APPLICATION = 'infinity_hub.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

if "DEV" in os.environ:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
else:
    DATABASES = {"default": dj_database_url.parse(
        os.environ.get("DATABASE_URL"))}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "/static/"
# STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = "/media/"
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
