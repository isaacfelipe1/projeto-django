"""
Django settings for django1 project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-qs$f5nc16i+w0#5d(^n2@ryeoha*fsi1ya4(0whfec8l@4e+5x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG =False # coloca False quandor for para Produção

ALLOWED_HOSTS = ['*']


# Application definition
#Aplicações Instalada
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
]
#MIDDlEWARE é de checagem
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
# Das rotas 
ROOT_URLCONF = 'django1.urls'
#Tudo que vamos mostrar para os usuarios (visivel para usuario)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'django1.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
#banco de dados
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'pt-br' # Linguagem da aplicação

TIME_ZONE = 'UTC'

USE_I18N = True # oferecer os sistemas em multiplos de idiomas

USE_TZ = True # configuração de typysom


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/' # diretórios do staticos ( "Qual o diretorio deles")
#Usado durante o desenvolvendo, para publicar na internet precisa criar outra variavel
STATIC_ROOT= os.path.join(BASE_DIR,'staticfiles') #usado durante a produção
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field
LOGOUT_REDIRECT_URL='index' # redireciona para página inicial da página

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'