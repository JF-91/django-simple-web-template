from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')
DEBUG = os.getenv('DJANGO_DEBUG', 'False') == 'True'

ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', '').split(',')


# Application definition

INSTALLED_APPS = [
    'django_daisy',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tailwind',
    'theme',
    'django_browser_reload',
    'page',
]

TAILWIND_APP_NAME = 'theme'

INTERNAL_IPS = [
    "127.0.0.1",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]

ROOT_URLCONF = 'config.urls'

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
                'page.context_processor.page_list',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE'),
        'NAME': BASE_DIR / os.getenv('DB_NAME'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = os.getenv('LANGUAGE_CODE')
TIME_ZONE = os.getenv('TIME_ZONE')
USE_I18N = os.getenv('USE_I18N') == 'True'
USE_TZ = os.getenv('USE_TZ') == 'True'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


## daizy settings
DAISY_SETTINGS = {
    'SITE_TITLE': os.getenv('DAISY_SITE_TITLE'),
    'SITE_HEADER': os.getenv('DAISY_SITE_HEADER'),
    'INDEX_TITLE': os.getenv('DAISY_INDEX_TITLE'),
    'SITE_LOGO': os.getenv('DAISY_SITE_LOGO'),
    'EXTRA_STYLES': [],  # List of extra stylesheets to be loaded in base.html (optional)
    'EXTRA_SCRIPTS': [],  # List of extra script URLs to be loaded in base.html (optional)
    'LOAD_FULL_STYLES': False,  # If True, loads full DaisyUI components in the admin (useful if you have custom template overrides)
    'SHOW_CHANGELIST_FILTER': False,  # If True, the filter sidebar will open by default on changelist views
    'DONT_SUPPORT_ME': False, # Hide github link in sidebar footer
    'SIDEBAR_FOOTNOTE': '', # add footnote to sidebar
    'APPS_REORDER': {
        # Custom configurations for third-party apps that can't be modified directly in their `apps.py`
        'auth': {
            'icon': 'fa-solid fa-person-military-pointing',  # FontAwesome icon for the 'auth' app
            'name': 'Authentication',  # Custom name for the 'auth' app
            'hide': False,  # Whether to hide the 'auth' app from the sidebar (set to True to hide)
            'app': 'users',  # The actual app to display in the sidebar (e.g., rename 'auth' to 'users')
            'divider_title': "Auth",  # Divider title for the 'auth' section
        },
        'social_django': {
            'icon': 'fa-solid fa-users-gear',  # Custom FontAwesome icon for the 'social_django' app
        },
    },
}