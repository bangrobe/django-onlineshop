from .base import *
from .base import env
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
       'ENGINE': env('SQL_ENGINE'),
       'NAME': env('SQL_DATABASE'),
       'USER': env('SQL_USER'),
       'PASSWORD': env('SQL_PASSWORD'),
       'HOST': env('SQL_HOST'),
       'PORT': env('SQL_PORT'),
    }
}

# Email for testing celery send mail - Chapter 8
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Setting Stripe - Chapter 9
STRIPE_PUBLISHABLE_KEY = 'pk_test_51IT1miEDhYmQiN9tbPNtCsZRRJ9ZH12cO7XUZEZCJFUqzqQfGdKTcgfNIWjnqiaYClOTcA16X5kFn9HojDTF1unm00RrxmhdM1' # Publishable key
STRIPE_SECRET_KEY = 'sk_test_51IT1miEDhYmQiN9tvAA2S73XyYb6DkWbYMC76B26hjWTo48GaH5i8VgqwByazb8e1s4CJwt6s6nEKu5csx65ihsh00nOZSLpGz' # Secret key
STRIPE_API_VERSION = '2022-08-01'
STRIPE_WEBHOOK_SECRET = 'whsec_b182e01f4f517cf8881748197d1be7b38b2a900d144f93193d391c71b9b6a3df'

INTERNAL_IPS = ["127.0.0.1", "10.0.2.2"]

# Redis - Chapter 10 - Page 468, recommend products
REDIS_HOST = env('REDIS_HOST')
REDIS_PORT = env('REDIS_PORT')
REDIS_DB=1
REDIS_URL =  f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}"

# CACHES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "",
    }
}


RABBITMQ = {
    "PROTOCOL": "amqp", # in prod change with "amqps"
    "HOST": os.getenv("RABBITMQ_HOST", "localhost"),
    "PORT": os.getenv("RABBITMQ_PORT", 5672),
    "USER": os.getenv("RABBITMQ_DEFAULT_USER", "guest"),
    "PASSWORD": os.getenv("RABBITMQ_DEFAULT_PASS", "guest"),
}

CELERY_BROKER_URL = f"{RABBITMQ['PROTOCOL']}://{RABBITMQ['USER']}:{RABBITMQ['PASSWORD']}@{RABBITMQ['HOST']}:{RABBITMQ['PORT']}"

