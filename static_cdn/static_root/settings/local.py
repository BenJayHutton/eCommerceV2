from .base import *
from dotenv import load_dotenv
load_dotenv()

# os.environ.get()
SECRET_KEY = os.environ.get("SECRET_KEY")
ALLOWED_HOSTS = ['192.168.10.3', 'localhost', '127.0.0.1']

AWS_ACCESS_KEY_ID=os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY=os.environ.get("AWS_SECRET_ACCESS_KEY")
DATABASE_URL=os.environ.get("DATABASE_URL")
DISABLE_COLLECTSTATIC=1
EMAIL_HOST_PASSWORD=os.environ.get("EMAIL_HOST_PASSWORD")
MAILCHIMP_API_KEY=os.environ.get("MAILCHIMP_API_KEY")
MAILCHIMP_EMAIL_LIST_ID=os.environ.get("MAILCHIMP_EMAIL_LIST_ID")
SECRET_KEY=os.environ.get("SECRET_KEY")
STRIPE_PUB_KEY=os.environ.get("STRIPE_PUB_KEY")
STRIPE_SECRET_API_KEY=os.environ.get("STRIPE_SECRET_API_KEY")

