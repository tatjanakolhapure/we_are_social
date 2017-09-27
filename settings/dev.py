from base import *

DEBUG = True

INSTALLED_APPS.append('debug_toolbar')
MIDDLEWARE_CLASSES.append('debug_toolbar.middleware.DebugToolbarMiddleware')

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
SITE_URL = 'http://127.0.0.1:8000'
PAYPAL_NOTIFY_URL = 'http://174a664b.ngrok.io/a-very-hard-to-guess-url/'
PAYPAL_RECEIVER_EMAIL = 'tatjanagkolhapure-facilitator@gmail.com'

# Debug Toolbar
INTERNAL_IPS = ('127.0.0.1',)