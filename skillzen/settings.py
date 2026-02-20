from pathlib import Path

# BASE DIRECTORY
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY KEY (keep as it is)
SECRET_KEY = 'django-insecure-skillzen-secret-key'


# DEBUG MODE (keep True for development)
DEBUG = True


# ALLOWED HOSTS
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']


# INSTALLED APPS
INSTALLED_APPS = [

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # YOUR APPS
    'payments',
    'accounts',

]


# MIDDLEWARE
MIDDLEWARE = [

    'django.middleware.security.SecurityMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.common.CommonMiddleware',

    'django.middleware.csrf.CsrfViewMiddleware',

    'django.contrib.auth.middleware.AuthenticationMiddleware',

    'django.contrib.messages.middleware.MessageMiddleware',

]


# ROOT URL FILE
ROOT_URLCONF = 'skillzen.urls'


# TEMPLATES
TEMPLATES = [
{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',

    'DIRS': [BASE_DIR / 'templates'],

    'APP_DIRS': True,

    'OPTIONS': {

        'context_processors': [

            'django.template.context_processors.debug',

            'django.template.context_processors.request',

            'django.contrib.auth.context_processors.auth',

            'django.contrib.messages.context_processors.messages',

        ],

    },

},
]


# WSGI APPLICATION
WSGI_APPLICATION = 'skillzen.wsgi.application'


# DATABASE (SQLite)
DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.sqlite3',

        'NAME': BASE_DIR / 'db.sqlite3',

    }

}


# PASSWORD VALIDATION
AUTH_PASSWORD_VALIDATORS = [

{
'name': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
},

{
'name': 'django.contrib.auth.password_validation.MinimumLengthValidator',
},

{
'name': 'django.contrib.auth.password_validation.CommonPasswordValidator',
},

{
'name': 'django.contrib.auth.password_validation.NumericPasswordValidator',
},

]


# LANGUAGE
LANGUAGE_CODE = 'en-us'


# TIME ZONE
TIME_ZONE = 'Asia/Kolkata'


# STATIC FILES (CSS, JS, Images)
STATIC_URL = '/static/'

STATICFILES_DIRS = [

BASE_DIR / 'static',

]


# DEFAULT PRIMARY KEY
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



#  UPI ID
UPI_ID = "srinathsri740@okhdfcbank"

# COMPANY NAME
UPI_NAME = "SkillZen"

# QR IMAGE LOCATION
QR_IMAGE = "D:\MCA\PROJECT\static\qr.png"