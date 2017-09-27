from base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_oV4e35Zirwo0wmm7ZrjgZO1k')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_wUTLcpVb8nhWmDxUhBKd0Yxc')

# PayPal Settings
PAYPAL_NOTIFY_URL = 'social-staging-code-institute.herokuapp.com'
PAYPAL_RECEIVER_EMAIL = 'tatjanagkolhapure-facilitator@gmail.com'

SITE_URL = 'social-staging-code-institute.herokuapp.com'
ALLOWED_HOSTS.append('social-staging-code-institute.herokuapp.com')

# Log DEBUG information to the console
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}