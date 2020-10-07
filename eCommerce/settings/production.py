from .base import *

# os.environ.get()
SECRET_KEY = os.environ.get("SECRET_KEY")
ALLOWED_HOSTS = ['.herokuapp.com']
AWS_ACCESS_KEY_ID=os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY=os.environ.get("AWS_SECRET_ACCESS_KEY")
DATABASE_URL=os.environ.get("DATABASE_URL")
DEBUG = False
DISABLE_COLLECTSTATIC=1
EMAIL_HOST_PASSWORD=os.environ.get("EMAIL_HOST_PASSWORD")
MAILCHIMP_API_KEY=os.environ.get("MAILCHIMP_API_KEY")
MAILCHIMP_EMAIL_LIST_ID=os.environ.get("MAILCHIMP_EMAIL_LIST_ID")
SECRET_KEY=os.environ.get("SECRET_KEY")
STRIPE_PUB_KEY=os.environ.get("STRIPE_PUB_KEY")
STRIPE_SECRET_API_KEY=os.environ.get("STRIPE_SECRET_API_KEY")

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

#Database settings for heroku in production
import dj_database_url
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)
DATABASES['default']['CONN_MAX_AGE'] = 500