"""
Django settings for marry project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+wym-^pz%rwx!7v+az0gwxxre)^_4&6*cig5%v+gj_x2rcgjd('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'booktest.apps.SuitConfig',  # 需要添加的内容，要放在'django.contrib.admin'之前  美化admin
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'booktest',
    #跨域配置
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware', #跨域问题 这个设置为中间件的第一条
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'marry.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [os.path.join(BASE_DIR,'templates')],
        'DIRS': [os.path.join(BASE_DIR,'vue-demo01/dist')],
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

WSGI_APPLICATION = 'marry.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "marry",
        'USER':"root",
        'PASSWORD':"hhhheeq",
        'HOST':"localhost",#连接本机数据库
        'PORT':"3306",
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = 'vue-demo01/dist/static/'
STATICFILES_DIRS=[
    os.path.join(BASE_DIR,'vue-demo01/dist/static')
    # os.path.join(BASE_DIR,'static')
]
# STATIC_URL = '/static/'
# STATICFILES_DIRS=[
#     os.path.join(BASE_DIR,'static')
# ]

# 允许所有域名跨域(优先选择)
CORS_ORIGIN_ALLOW_ALL = True   # 这里可以设置白名单


#邮箱验证码配置
EMAIL_HOST = 'smtp.qq.com'
EMAIL_PORT = 25     #发件箱的smtp服务器端口
EMAIL_HOST_USER = '1755457338@qq.com' # 你的 QQ 账号
EMAIL_HOST_PASSWORD = 'nhctcsrayyiwbica'#授权码
EMAIL_USE_TLS = True # 这里必须是 True，否则发送不成功
EMAIL_FROM = '1755457338@qq.com'  # 你的 QQ 账号

# 配置上传文件存放的路径
MEDIA_URL = '/static/'
# 指定的文件存放的根目录，是一个字符串路径
#设置静态文件路径为主目录下的media文件夹
MEDIA_ROOT = os.path.join(BASE_DIR, 'static').replace("\\","/")    
