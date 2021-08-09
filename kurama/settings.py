import os
from enum import Enum


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'hh^3gwexfrdfe6@c7)7u5oi(ift1jmh@0ep*9mea$d8c07u8g9'
DEBUG = True
ALLOWED_HOSTS = []
ROOT_URLCONF = 'kurama.urls'
WSGI_APPLICATION = 'kurama.wsgi.application'
STATIC_URL = '/static/'

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

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Real time assets:

class Assets(Enum):
    BTC = 1
    BCH = 2
    ETH = 3
    LTC = 4
    CHZ = 5
    XRP = 6
    PAXG = 7
    JUVFT = 8
    PSGFT = 9
    MBVASCO01 = 10
    AAVE = 11
    ACMFT = 12
    ASRFT = 13
    ATMFT = 14
    AXS = 15
    BAL = 16
    BAT = 17
    CAIFT = 18
    MBPRK01 = 19
    MBPRK02 = 20
    MBPRK03 = 21
    MBPRK04 = 22
    MCO2 = 23
    USDC = 24
    WBX = 25

class Method():
    TICKER = 'ticker'
    TRADES = 'trades'
    DAY_SUMMARY = 'day-summary'
    TICKER_HIGH = 'high'
    TICKER_LOW = 'low'
    TICKER_BUY = 'buy'
    TICKER_SELL = 'sell'
    TICKER_LAST = 'last'
    DAY_SUMMARY_OPENING = 'opening'
    DAY_SUMMARY_CLOSING = 'closing'
    DAY_SUMMARY_HIGHEST = 'highest'
    DAY_SUMMARY_LOWEST = 'lowest'
