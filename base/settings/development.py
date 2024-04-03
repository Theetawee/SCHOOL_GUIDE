from base.settings.base import *


DEBUG = True

ALLOWED_HOSTS = ["*"]


STATIC_URL = "static/"
MEDIA_URL = "media/"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    os.path.join(BASE_DIR, "media"),
]
STATIC_ROOT = os.path.join(BASE_DIR, "static_cdn")

MEDIA_ROOT = os.path.join(BASE_DIR, "media_cdn")

INTERNAL_IPS = [
    "127.0.0.1",
]

BACKUP_DIRECTORY = os.path.join(BASE_DIR, "backups/development")


ACCOUNT_DEFAULT_HTTP_PROTOCOL = "http"


SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "SCOPE": [
            "profile",
            "email",
        ],
        "AUTH_PARAMS": {
            "access_type": "online",
        },
        "OAUTH_PKCE_ENABLED": True,
        "APP": {"client_id": "123", "secret": "456", "key": ""},
    }
}
