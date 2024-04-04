from base.settings.base import *

DEBUG = False

ALLOWED_HOSTS = ["*"]


# Replace the DATABASES section of your settings.py with this
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("PGDATABASE"),
        "USER": os.environ.get("PGUSER"),
        "PASSWORD": os.environ.get("PGPASSWORD"),
        "HOST": os.environ.get("PGHOST"),
        "PORT": os.environ.get("PGPORT", 5432),
        "OPTIONS": {
            "sslmode": "require",
        },
    }
}


CLOUDINARY_STORAGE = {
    "CLOUD_NAME": "dnb8rethz",
    "API_KEY": "123456789",
    "API_SECRET": os.environ.get("API_SECRET"),
}

DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"

STATIC_URL = "https://theetawee.github.io/static_cdn/"

BACKUP_DIRECTORY = os.path.join(BASE_DIR, "backups/production")

ACCOUNT_DEFAULT_HTTP_PROTOCOL = "https"

IS_PRODUCTION=True

SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "EMAIL_AUTHENTICATION": True,
        "SCOPE": [
            "profile",
            "email",
        ],
        "AUTH_PARAMS": {
            "access_type": "offline",
        },
        "FETCH_USERINFO": True,
        "OAUTH_PKCE_ENABLED": True,
        "APP": {
            "client_id": "914307882823-crg95miqt8572mtrvimh3rs2b9ujtep9.apps.googleusercontent.com",
            "secret": os.environ.get("GOOGLE_PROD"),
            "key": "",
        },
    }
}
