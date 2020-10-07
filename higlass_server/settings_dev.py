
from .settings_base import *


DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
]

if 'SITE_URL' in os.environ:
    ALLOWED_HOSTS += [os.environ['SITE_URL']]

# make all loggers use the console.
for logger in LOGGING['loggers']:
    LOGGING['loggers'][logger]['handlers'] = ['console']


CORS_ORIGIN_ALLOW_ALL = False
CORS_ALLOW_CREDENTIALS = True

CORS_ORIGIN_WHITELIST = [
    'http://localhost:8080',
    'http://localhost:6543'
]

SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

