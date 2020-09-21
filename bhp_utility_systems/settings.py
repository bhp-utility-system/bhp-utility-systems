"""
Django settings for bhp_utility_systems project.

Generated by 'django-admin startproject' using Django 3.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

APP_NAME = 'bhp_utility_systems'

INDEX_PAGE = 'bhpus.bhp.org.bw'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8g!)(+a#0*pv1n+ui5*dqw2axymk+)dh=^3zec#n4sels7!h1p'

# SECURITY WARNING: don't run with debug turned on in production!

ETC_DIR = '/etc/'

SITE_ID = 40

LOGIN_REDIRECT_URL = 'home_url'

DEBUG = True

ALLOWED_HOSTS = ['bhpus.bhp.org.bw', 'localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_crypto_fields.apps.AppConfig',
    'django_extensions',
    'edc_dashboard.apps.AppConfig',
    'edc_device.apps.AppConfig',
    'edc_model_admin.apps.AppConfig',
    'edc_navbar.apps.AppConfig',
    'procurement_dashboard.apps.AppConfig',
    'procurement.apps.AppConfig',
    'bhp_personnel.apps.AppConfig',
    'cms_dashboard.apps.AppConfig',
    'bhp_utility_systems.apps.EdcBaseAppConfig',
    'bhp_utility_systems.apps.EdcProtocolAppConfig',
    'bhp_utility_systems.apps.EdcIdentifierAppConfig',
    'bhp_utility_systems.apps.AppConfig',
    'document_tracking.apps.AppConfig',
    'document_tracking_dashboard.apps.AppConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'edc_dashboard.middleware.DashboardMiddleware',
    'edc_subject_dashboard.middleware.DashboardMiddleware'
]

ROOT_URLCONF = 'bhp_utility_systems.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'bhp_utility_systems.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_CODE = '40'

DEFAULT_STUDY_SITE = '40'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'bhp_utility_systems', 'static')

# Dashboards

DASHBOARD_URL_NAMES = {
    'document_listboard_url': 'document_tracking_dashboard:document_listboard_url',
    'document_url': 'document_tracking_dashboard:document_url',
    'procurement_url': 'procurement_dashboard:procurement_url',
    'purchase_order_listboard_url': 'procurement_dashboard:purchase_order_listboard_url',
    'purchase_order_report_url': 'procurement_dashboard:purchase_order_report_url',
    # CMS url name
    'employee_dashboard_url': 'cms_dashboard:employee_dashboard_url',
    'employee_listboard_url': 'cms_dashboard:employee_listboard_url',
    'emp_contract_listboard_url': 'cms_dashboard:emp_contract_listboard_url',
    'pi_contract_listboard_url': 'cms_dashboard:pi_contract_listboard_url',
    'pi_listboard_url': 'cms_dashboard:pi_listboard_url',
    'pi_dashboard_url': 'cms_dashboard:pi_dashboard_url',
    'consultant_contract_listboard_url': 'cms_dashboard:'
                                         'consultant_contract_listboard_url',
    'consultant_listboard_url': 'cms_dashboard:consultant_listboard_url',
    'consultant_dashboard_url': 'cms_dashboard:consultant_dashboard_url',
    'contract_listboard_url': 'cms_dashboard:contract_listboard_url',
    'cms_url': 'cms_dashboard:cms_url'
}

LAB_DASHBOARD_URL_NAMES = {}

DASHBOARD_BASE_TEMPLATES = {
    'listboard_base_template': 'bhp_utility_systems/base.html',
    'document_listboard_template': 'document_tracking_dashboard/document/document_listboard.html',
    'purchase_order_listboard_template': 'procurement_dashboard/purchase_order/listboard.html',
    'purchase_order_report_template': 'procurement_dashboard/purchase_order/report.html',
    # CMS templates
    'contract_listboard_template': 'cms_dashboard/contract/contract_listboard.html',
    'allcontracts_listboard_template': 'cms_dashboard/contract/'
                                       'allcontracts_listboard.html',
    'dashboard_base_template': 'cms/base.html',
    'employee_dashboard_template': 'cms_dashboard/employee/employee_dashboard.html',
    'employee_listboard_template': 'cms_dashboard/employee/employee_listboard.html',
    'pi_dashboard_template': 'cms_dashboard/pi/pi_dashboard.html',
    'pi_listboard_template': 'cms_dashboard/pi/pi_listboard.html',
    'consultant_listboard_template': 'cms_dashboard/consultant/consultant_listboard.html',
    'consultant_dashboard_template': 'cms_dashboard/consultant/consultant_dashboard.html',
}

CRISPY_TEMPLATE_PACK = 'bootstrap3'
GIT_DIR = BASE_DIR

