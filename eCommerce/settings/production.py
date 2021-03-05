from .base import *
from eCommerce.aws.conf import *
import dj_database_url

db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)
DATABASES['default']['CONN_MAX_AGE'] = 500

# Project settings
ALLOWED_HOSTS = ['.herokuapp.com', '.sweetsweetswag.com']
DATABASE_URL = os.environ.get("DATABASE_URL")
DEBUG = False
DISABLE_COLLECTSTATIC = 1
SECRET_KEY=os.environ.get("SECRET_KEY")


#Email Settings
EMAIL_HOST = os.environ.get("EMAIL_HOST", None)
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER", None)
EMAIL_HOST_PASSWORD=os.environ.get("EMAIL_HOST_PASSWORD", None)
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = os.environ.get("DEFAULT_FROM_EMAIL", None)
BASE_URL = os.environ.get("BASE_URL", None)
DEFAULT_ACTIVATION_DAYS = 1
MANAGER = os.environ.get("MANAGER",None)
MANAGER_NAME = os.environ.get("MANAGER_NAME",None)

ADMINS = [
    (MANAGER_NAME, MANAGER),
]

#Mailchimp Settings
MAILCHIMP_API_KEY = os.environ.get("MAILCHIMP_API_KEY")
MAILCHIMP_EMAIL_LIST_ID = os.environ.get("MAILCHIMP_EMAIL_LIST_ID")

#Stripe Settings
STRIPE_PUB_KEY = os.environ.get("STRIPE_PUB_KEY")
STRIPE_SECRET_API_KEY = os.environ.get("STRIPE_SECRET_API_KEY")


#security settings for production.py:
CORS_REPLACE_HTTPS_REFERER      = True
HOST_SCHEME                     = "https://"
SECURE_PROXY_SSL_HEADER         = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT             = True
SESSION_COOKIE_SECURE           = True
CSRF_COOKIE_SECURE              = True
SECURE_HSTS_INCLUDE_SUBDOMAINS  = True
SECURE_HSTS_SECONDS             = 1000000
SECURE_FRAME_DENY               = True
