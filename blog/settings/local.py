from decouple import config

from .base import *

DEBUG = True
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = config(
    "DJANGO_SECRET_KEY", default="!!!SET DJANGO_SECRET_KEY!!!", cast=str
)
# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

STATIC_DIRECTORY = "/static/"
MEDIA_DIRECTORY = "/media/"
MEDIA_ROOT = f"{BASE_DIR}/media/"
