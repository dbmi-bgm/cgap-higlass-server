
from .settings_base import *

DEBUG = False

ALLOWED_HOSTS = [
    'cgap-higlass.com',
]

if 'SITE_URL' in os.environ:
    ALLOWED_HOSTS += [os.environ['SITE_URL']]

CORS_ORIGIN_ALLOW_ALL = False
CORS_ALLOW_CREDENTIALS = True

CORS_ORIGIN_WHITELIST = [
    'https://cgap.hms.harvard.edu'
]

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

