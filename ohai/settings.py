from os import path, getenv
BASE_DIR = path.dirname(path.dirname(__file__))

PROJECT = 'ohai'

SECRET_KEY = getenv('SECRET_KEY', 'changeme')
DEBUG = getenv('DEBUG', False)

ALLOWED_HOSTS = []

# Email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
ADMINS = (
    (
        getenv('ADMINS_FROM_NAME', 'Admins'),
        getenv('ADMINS_FROM_EMAIL', 'noreply@example.com')
    ),
)
MANAGERS = ADMINS
DEFAULT_FROM_EMAIL = getenv('DEFAULT_FROM_EMAIL', 'noreply@example.com')
SERVER_EMAIL = DEFAULT_FROM_EMAIL

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_markdown',
    'easy_thumbnails',
    'ohai_kit'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'ohai.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [path.join(BASE_DIR, PROJECT, '/templates')],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
        },
    },
]

WSGI_APPLICATION = 'ohai.wsgi.application'

# Database
import dj_database_url
DATABASE_URL = getenv('DATABASE_URL', 'sqlite:///db.sqlite3')
DATABASES = {'default': dj_database_url.parse(DATABASE_URL)}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = False
USE_L10N = False
USE_TZ = True

STATIC_ROOT = path.join(path.dirname(BASE_DIR), PROJECT, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    path.join(BASE_DIR, PROJECT, 'static'),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = path.join(BASE_DIR, PROJECT, 'static')

GOOGLE_ANALYTICS_KEY = getenv('GOOGLE_ANALYTICS_KEY', None)
