from django.conf import global_settings
"""
Django settings for studentsdb project.

Generated by 'django-admin startproject' using Django 1.9.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'jvx01kih(l^8u^yu0l$m6&#z8z8w4)ijny)e28#av9)my%&yk!'

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
    'crispy_forms',
    'registration',
    'students',
]

MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'studentsdb.urls'

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

WSGI_APPLICATION = 'studentsdb.wsgi.application'


from .database import DATABASES



# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'uk-Uk'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
TEMPLATE_CONTEXT_PROCESSORS = \
global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
"django.core.context_processors.request",
"students.context_processors.groups_processor",
"students.context_processors.lang_processor",
"students.context_processors.stud_c"
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '..', 'media')

from .mail import *


###########################

#loggers
LOG_FILE = os.path.join(BASE_DIR, 'studentsdb.log')
LOG_FILE2 = os.path.join(BASE_DIR, 'mail_errors')

LOGGING = {
	'version': 1,
	'disable_existing_loggers': True,
	'formatters': {
	'verbose': {
	  'format': '%(levelname)s %(asctime)s %(module)s: %(message)s'
	  },
	  'simple': {
	    'format': '%(levelname)s: %(message)s'
	  },
   },
   'handlers': {
     'null': {
       'level': 'DEBUG',
       'class': 'logging.NullHandler',
     },
     'console': {
       'level': 'INFO',
       'class': 'logging.StreamHandler',
       'formatter': 'verbose',
     },
     'mail_admins': {
       'level': 'INFO',
       'class': 'django.utils.log.AdminEmailHandler',
       'email_backend': 'django.core.mail.backends.smtp.EmailBackend',
            
     },
     'file': {
     'level': 'INFO',
     'class': 'logging.FileHandler',
     'filename': LOG_FILE,
     'formatter': 'verbose'
     },
     'file2': {
     'level': 'INFO',
     'class': 'logging.FileHandler',
     'filename': LOG_FILE2,
     'formatter': 'verbose'
     },
     'database': {
            'level': 'DEBUG',
            'class': 'studentsdb.custom_handlers.DatabaseHandler',
            'formatter': 'verbose'
     },
   },
   'loggers': {
     'django': {
       'handlers': ['null'],
       'propagate': True,
       'level': 'INFO',
     },
     'students.signals': {
     'handlers': ['file','console', 'mail_admins', 'database'],
     'level': 'INFO',
     },
     'students.view.contact_admin': {
     'handlers': ['file2', 'mail_admins'],
     'level': 'INFO',
     }

   }
}

REGISTRATION_OPEN = True

