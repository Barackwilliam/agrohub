"""
East Africa AgroHub Export Ltd - Django Settings
"""

import os
from pathlib import Path
import dj_database_url
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-change-this-in-production-agrohub-2024')

DEBUG = False

ALLOWED_HOSTS = ['*', 'eastafricaagrohub.com', 'www.eastafricaagrohub.com', '.onrender.com']

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Local apps
    'core',
    'products',
    'siteconfig',
    'inquiries',
]

JAMIITEK_API_KEY = "So8q1wsIl8tmM2x8h_mbh0Il_n5yKtXEBuju5w3-2_dQOPeEEYjGsFbnwTibXds2"
JAMIITEK_API_URL = "https://jamiitek.com/api/site-status/"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'jamiitek_middleware.JamiiTekStatusMiddleware',
]

ROOT_URLCONF = 'agrohub.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'siteconfig.context_processors.site_settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'agrohub.wsgi.application'


#Database from minanicharles14@gmail.com

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres', 
        'USER': 'postgres.ijzzqjoggkmrryhgueom',  
        'PASSWORD': 'NyumbaChap@123', 
        'HOST': 'aws-1-us-east-2.pooler.supabase.com',  
        'PORT': '5432',  
    }
}



# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }



UPLOADCARE = {
    'pub_key': 'cff49d484a4e0a5d423f',
    'secret': 'f536e03e075f3a690e32',
}


AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Africa/Dar_es_Salaam'
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
DEFAULT_FROM_EMAIL = 'East Africa AgroHub <export@eastafricaagrohub.co.tz>'

# Jazzmin Admin UI Configuration
JAZZMIN_SETTINGS = {
    "site_title": "AgroHub Admin",
    "site_header": "East Africa AgroHub",
    "site_brand": "AgroHub Export",
    "site_logo": None,
    "site_logo_classes": "img-circle",
    "site_icon": None,
    "welcome_sign": "Welcome to East Africa AgroHub Admin Panel",
    "copyright": "East Africa AgroHub Export Ltd",
    "search_model": ["auth.user", "products.Product", "inquiries.Inquiry"],
    "user_avatar": None,
    "topmenu_links": [
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "View Website", "url": "/", "new_window": True},
    ],
    "usermenu_links": [
        {"name": "View Website", "url": "/", "new_window": True},
    ],
    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": [],
    "hide_models": [],
    "order_with_respect_to": [
        "siteconfig",
        "core",
        "products",
        "inquiries",
        "auth",
    ],
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "products.Product": "fas fa-seedling",
        "products.ProductCategory": "fas fa-tags",
        "inquiries.Inquiry": "fas fa-envelope",
        "siteconfig.SiteSettings": "fas fa-cog",
        "siteconfig.HeroSlide": "fas fa-images",
        "siteconfig.WhyChooseUs": "fas fa-star",
        "siteconfig.CoreValue": "fas fa-gem",
        "siteconfig.SocialLink": "fas fa-share-alt",
    },
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    "related_modal_active": False,
    "custom_css": None,
    "custom_js": None,
    "use_google_fonts_cdn": True,
    "show_ui_builder": False,
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "auth.group": "vertical_tabs",
    },
    "language_chooser": False,
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-success",
    "accent": "accent-teal",
    "navbar": "navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": "sidebar-dark-success",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "darkly",
    "dark_mode_theme": "darkly",
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    },
}
