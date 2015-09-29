# omret
prename is r305


### settings.py
<pre>
# Django settings for omret project.

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS


#----config database-------
from os import environ
debug = not environ.get("APP_NAME","")
if debug:
    #LOCALMY
    MYSQL_DB = "app_omret"
    MYSQL_USER = "***"
    MYSQL_PASS = "**********"
    MYSQL_HOST_M = "*****"
    MYSQL_PORT = "*****"
    
else:
    import sae.const
    MYSQL_DB = sae.const.MYSQL_DB
    MYSQL_USER = sae.const.MYSQL_USER
    MYSQL_PASS = sae.const.MYSQL_PASS
    MYSQL_HOST_M = sae.const.MYSQL_HOST
    MYSQL_PORT = sae.const.MYSQL_PORT
    MYSQL_HOST_S = sae.const.MYSQL_HOST_S

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': MYSQL_DB,                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': MYSQL_USER,
        'PASSWORD': MYSQL_PASS,
        'HOST': MYSQL_HOST_M,                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': MYSQL_PORT,                      # Set to empty string for default.
    }
}


ALLOWED_HOSTS=['www.omret.com','omret.sinaapp.com','omret.vipsinaapp.com']

TIME_ZONE = 'Asia/Shanghai'

LANGUAGE_CODE = 'zh-cn'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = ''

MEDIA_URL = ''

STATIC_ROOT = ''

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = '**************************'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'omret.urls'

WSGI_APPLICATION = 'omret.wsgi.application'

import os
FILE_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(FILE_PATH)+"/"
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,'templates/'),
    os.path.join(BASE_DIR,'templates/logreg/'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'omret',
    'omret.logreg',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

##--------send email config----------
EMAIL_HOST = 'smtp.sina.com.cn'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'omret@sina.com'
EMAIL_HOST_PASSWORD = '*********'
EMAIL_SUBJECT_PREFIX = u'[Omret]'
EMAIL_USE_TLS = True

SERVER_EMAIL = 'omret@sina.com'
DEFAULT_CHARSET = 'utf-8'
</pre>
