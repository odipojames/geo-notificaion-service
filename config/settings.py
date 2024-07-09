from pathlib import Path
from datetime import timedelta
import os
import dj_database_url
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = os.environ.get('DEBUG') == 'True'  # Convert to boolean

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'notifications',
    'rest_framework_swagger',
    'drf_yasg',
]

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

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'

# Database
MODE = os.environ.get('MODE')
if MODE == "prod":
    DATABASES = {"default": dj_database_url.config(default=os.getenv("DATABASE_URL"))}
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = "Africa/Nairobi"
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# Remove or comment out STATICFILES_DIRS if not using
# STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build', 'static')

# Add this for whitenoise
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# SWAGGER_SETTINGS to ensure proper display of the UI
SWAGGER_SETTINGS = {
    "SECURITY_DEFINITIONS": {
        "Bearer": {"type": "apiKey", "name": "Authorization", "in": "header"}
    },
    "USE_SESSION_AUTH": False,
    "DOC_EXPANSION": "none",
    "SHOW_REQUEST_HEADERS": True,
    "OPERATIONS_SORTER": "alpha",
    "JSON_EDITOR": True,
    "DEFAULT_MODEL_RENDERING": "example",
}

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTTokenUserAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 5
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=24),
    'SIGNING_KEY': os.environ.get('SIGNING_KEY'),
}
