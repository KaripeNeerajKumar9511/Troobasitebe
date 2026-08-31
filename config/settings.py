from pathlib import Path
import os

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "dev-only-change-me")
DEBUG = os.getenv("DEBUG", "true").lower() in ("1", "true", "yes")
ALLOWED_HOSTS = [
    h.strip()
    for h in os.getenv("ALLOWED_HOSTS", "localhost,127.0.0.1").split(",")
    if h.strip()
]

FRONTEND_ORIGIN = os.getenv("FRONTEND_ORIGIN", "http://localhost:3000")
ADMIN_ORIGIN = os.getenv("ADMIN_ORIGIN", "http://localhost:3001")
FRONTEND_CONTENT_DIR = Path(
    os.getenv(
        "FRONTEND_CONTENT_DIR",
        str(BASE_DIR.parent / "Frontend" / "src" / "content"),
    )
)

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "corsheaders",
    "cms",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    }
]

WSGI_APPLICATION = "config.wsgi.application"

# PostgreSQL only. Prefer explicit DB_* vars in .env (SQLite is not supported).
DB_ENGINE = os.getenv("DB_ENGINE", "django.db.backends.postgresql")
if "sqlite" in DB_ENGINE.lower() or os.getenv("DATABASE_URL", "").startswith("sqlite"):
    raise RuntimeError("SQLite is not supported. Use PostgreSQL via DB_* in .env.")
if "postgresql" not in DB_ENGINE and "postgres" not in DB_ENGINE:
    raise RuntimeError(f"DB_ENGINE must be PostgreSQL, got {DB_ENGINE!r}")

DATABASES = {
    "default": {
        "ENGINE": DB_ENGINE,
        "NAME": os.getenv("DB_NAME", "trooba"),
        "USER": os.getenv("DB_USER", "trooba"),
        "PASSWORD": os.getenv("DB_PASSWORD", ""),
        "HOST": os.getenv("DB_HOST", "localhost"),
        "PORT": os.getenv("DB_PORT", "5432"),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CORS_ALLOWED_ORIGINS = [
    origin
    for origin in (
        FRONTEND_ORIGIN,
        ADMIN_ORIGIN,
        os.getenv("EXTRA_CORS_ORIGIN", ""),
    )
    if origin
]
CORS_ALLOW_CREDENTIALS = True

CSRF_TRUSTED_ORIGINS = CORS_ALLOWED_ORIGINS

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticated",
    ),
}

from datetime import timedelta

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(hours=12),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "SIGNING_KEY": os.getenv("JWT_SECRET", SECRET_KEY),
}

ADMIN_SEED_EMAIL = os.getenv("ADMIN_EMAIL", "admin@trooba.com")
ADMIN_SEED_PASSWORD = os.getenv("ADMIN_PASSWORD", "changeme")
