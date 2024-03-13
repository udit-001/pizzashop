from .base import *

env.read_env(os.path.join(BASE_DIR, '.env'))

# For making allauth work without setting up an smtp server
EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend"
)

INSTALLED_APPS += ["django_extensions"]
