from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-tcmr$pf(#b(vfr_aytbz02)tg0v0vkpas(f7oc)5a8qdlq(wga"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

INSTALLED_APPS = INSTALLED_APPS + [
    "debug_toolbar"
]

# TEMPLATES = TEMPLATES + [
#     {
#         "BACKEND": "django.template.backends.django.DjangoTemplates",
#         "APP_DIRS": True,
#     },

# ]

# MIDDLEWARE = MIDDLEWARE = [
#     "debug_toolbar.middleware.DebugToolbarMiddleware",
# ]

INTERNAL_IPS = INTERNAL_IPS = [
    "127.0.0.1",
]

try:
    from .local import *
except ImportError:
    pass
