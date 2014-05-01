"""
Django settings for agrocal project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'wym^voa0dd0ctdeuio4yqn!e!e#0o@tdoid7f4uewmb96-4vh('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'principal',
    'cuenta',
    'empleados',
    'clientes',
    'producto',
    'proveedores',
    'reportes',
    'factura',
<<<<<<< HEAD
=======
    'inventario',
>>>>>>> 7c6f7ebb9828b38cdb02b715888e268a54ec46f6
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

)

ROOT_URLCONF = 'agrocal.urls'

TEMPLATE_DIRS = (

    os.path.join(BASE_DIR, 'agrocal', 'templates'),
    os.path.join(BASE_DIR, 'principal','templates'),
    os.path.join(BASE_DIR, 'cuenta','templates'),
    os.path.join(BASE_DIR, 'empleados','templates'),
    os.path.join(BASE_DIR, 'clientes','templates'),
    os.path.join(BASE_DIR, 'producto','templates'),
    os.path.join(BASE_DIR, 'proveedores','templates'),
    os.path.join(BASE_DIR, 'reportes','templates'),
    os.path.join(BASE_DIR, 'factura','templates'),
    )

WSGI_APPLICATION = 'agrocal.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es-hn'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

MEDIA_ROOT = os.path.join(BASE_DIR, 'agrocal', 'resources')
MEDIA_URL = '/resources/'

STATIC_ROOT = os.path.join(BASE_DIR, 'agrocal', 'static')
<<<<<<< HEAD
STATIC_URL = '/static/'
=======
STATIC_URL = '/static/'
>>>>>>> 7c6f7ebb9828b38cdb02b715888e268a54ec46f6
