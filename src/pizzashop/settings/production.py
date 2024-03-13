from .base import *

DEBUG = False

MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware', )

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Security
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'

# Email SMTP Settings
EMAIL_HOST = env('EMAIL_HOST', default='smtp.sendgrid.net')
EMAIL_PORT = env('EMAIL_PORT', default='587')
EMAIL_HOST_USER = env('EMAIL_HOST_USER', default='apikey')
SENDGRID_API = env('SENDGRID_API', default=None)

if SENDGRID_API is None:
    EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
else:
    EMAIL_HOST_PASSWORD = env('SENDGRID_API')

EMAIL_USE_TLS = env('EMAIL_USE_TLS', default=True)
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL', default='mail@example.com')
