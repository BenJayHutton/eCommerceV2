from .base import *

#Django settings
SECRET_KEY = os.environ.get("SECRET_KEY")
ALLOWED_HOSTS = ['localhost', '127.0.0.1']
DEBUG = True

#Heroku Settings
DATABASE_URL = os.environ.get("DATABASE_URL")
DISABLE_COLLECTSTATIC = 1

#Email Settings
EMAIL_HOST = os.environ.get("EMAIL_HOST", None)
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER", None)
EMAIL_HOST_PASSWORD=os.environ.get("EMAIL_HOST_PASSWORD", None)
EMAIL_USE_TLS = True
EMAIL_TIMEOUT = 600
DEFAULT_FROM_EMAIL = os.environ.get("DEFAULT_FROM_EMAIL", None)
BASE_URL = os.environ.get("BASE_URL_LOCAL", None)
DEFAULT_ACTIVATION_DAYS = 1
MANAGER = os.environ.get("MANAGER",None)
MANAGER_NAME = os.environ.get("MANAGER_NAME",None)

ADMINS =[
    (MANAGER_NAME, MANAGER),
]


#Mailchimp settings
MAILCHIMP_API_KEY = os.environ.get("MAILCHIMP_API_KEY")
MAILCHIMP_EMAIL_LIST_ID = os.environ.get("MAILCHIMP_EMAIL_LIST_ID")
MAILCHIMP_DATA_CENTER = os.environ.get("MAILCHIMP_DATA_CENTER")

#Stripe settings
STRIPE_PUB_KEY = os.environ.get("STRIPE_PUB_KEY")
STRIPE_SECRET_API_KEY = os.environ.get("STRIPE_SECRET_API_KEY")

#settings for local.py
CORS_REPLACE_HTTPS_REFERER      = False
HOST_SCHEME                     = "http://"
SECURE_PROXY_SSL_HEADER         = None
SECURE_SSL_REDIRECT             = False
SESSION_COOKIE_SECURE           = False
CSRF_COOKIE_SECURE              = False
SECURE_HSTS_SECONDS             = None
SECURE_HSTS_INCLUDE_SUBDOMAINS  = False
SECURE_FRAME_DENY               = False

from eCommerce.aws.conf import *
