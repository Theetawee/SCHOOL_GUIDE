from base.settings.base import *

DEBUG = False

ALLOWED_HOSTS = [""]


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "neondb",
        "USER": "foreverinc",
        "PASSWORD": os.environ.get("DB_PASSWORD"),
        "HOST": "ep-blue-violet-792186.us-east-2.aws.neon.tech",
        "PORT": "5432",
    }
}

CLOUDINARY_STORAGE = {
    "CLOUD_NAME": "dnb8rethz",
    "API_KEY": "123456789",
    "API_SECRET": os.environ.get("API_SECRET"),
}

DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"

STATIC_URL = os.environ.get("STATIC_URL")

BACKUP_DIRECTORY = os.path.join(BASE_DIR, "backups/production")
