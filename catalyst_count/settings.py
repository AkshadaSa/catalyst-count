import os
from pathlib import Path
import environ

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
env.read_env(os.path.join(BASE_DIR, '.env'))

print("DB_NAME:", env('DB_NAME', default='default_value'))
print("DB_USER:", env('DB_USER', default='default_value'))
print("DB_PASSWORD:", env('DB_PASSWORD', default='default_value'))
print("DB_HOST:", env('DB_HOST', default='default_value'))
print("DB_PORT:", env('DB_PORT', default='default_value'))

# Security settings
SECRET_KEY = env('SECRET_KEY', default='your-secret-key')
DEBUG = env.bool('DEBUG', default=True)
ALLOWED_HOSTS = ['localhost', '127.0.0.1']




INSTALLED_APPS = [

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',  # Add your app here
    'django.contrib.sites',  # Required for allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'allauth.account.middleware.AccountMiddleware',  # Add this line
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'catalyst_count.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'catalyst_count.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'catalyst_db',
        'USER': 'catalyst_user',
        'PASSWORD': 'Avinash@92',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}


SITE_ID = 1

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

LOGIN_REDIRECT_URL = '/'

# URL prefix for static files
STATIC_URL = '/static/'

# Directory where static files will be collected for production
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Additional directories to look for static files
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'