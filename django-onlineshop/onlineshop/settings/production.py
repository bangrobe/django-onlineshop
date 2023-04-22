from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = env("DEBUG")

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Email for testing celery send mail - Chapter 8
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Setting Stripe - Chapter 9
STRIPE_PUBLISHABLE_KEY = 'pk_test_51IT1miEDhYmQiN9tbPNtCsZRRJ9ZH12cO7XUZEZCJFUqzqQfGdKTcgfNIWjnqiaYClOTcA16X5kFn9HojDTF1unm00RrxmhdM1' # Publishable key
STRIPE_SECRET_KEY = 'sk_test_51IT1miEDhYmQiN9tvAA2S73XyYb6DkWbYMC76B26hjWTo48GaH5i8VgqwByazb8e1s4CJwt6s6nEKu5csx65ihsh00nOZSLpGz' # Secret key
STRIPE_API_VERSION = '2022-08-01'
STRIPE_WEBHOOK_SECRET = 'whsec_b182e01f4f517cf8881748197d1be7b38b2a900d144f93193d391c71b9b6a3df'

INTERNAL_IPS = [
    "127.0.0.1",
]

# Redis - Chapter 10 - Page 468, recommend products
REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = os.getenv("REDIST_PORT", 6379)
REDIS_DB = 1


RABBITMQ = {
    "PROTOCOL": "amqp", # in prod change with "amqps"
    "HOST": os.getenv("RABBITMQ_HOST", "localhost"),
    "PORT": os.getenv("RABBITMQ_PORT", 5672),
    "USER": os.getenv("RABBITMQ_DEFAULT_USER", "guest"),
    "PASSWORD": os.getenv("RABBITMQ_DEFAULT_PASS", "guest"),
}

CELERY_BROKER_URL = f"{RABBITMQ['PROTOCOL']}://{RABBITMQ['USER']}:{RABBITMQ['PASSWORD']}@{RABBITMQ['HOST']}:{RABBITMQ['PORT']}"

