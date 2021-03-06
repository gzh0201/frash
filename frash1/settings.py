"""
Django settings for frash1 project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 't2q9i#%!^c2to4p%mdf4(-$vhs3sk3l0)#s)=_-9f%!w-2$tmx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app1',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'frash1.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'frash1.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static').replace('\\', '/')

# 日志
if os.path.exists(os.path.join(BASE_DIR, 'logs')) is False:
    os.mkdir(os.path.join(BASE_DIR, 'logs'))

BASE_LOG_DIR = os.path.join(BASE_DIR, "log")
LOGGING = {
	'version': 1, # 保留字
	'disable_existing_loggers': False, # 禁用已经存在的logger实例
	# 日志文件的格式
	'formatters': {
		# 详细的日志格式
		'standard': {
			'format': '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]'
            '[%(levelname)s][%(message)s]'
		},
		# 简单的日志格式
		'simple': {
			'format': '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'
		},
		# 定义一个特殊的日志格式
		'collect': {
			'format': '%(message)s'
		}
	},
	# 过滤器
	'filters': {
		'require_debug_true': {
			'()': 'django.utils.log.RequireDebugTrue',
		},
	},
    # 处理器
    'handlers': {
    # 在终端打印
    	'console': {
    		'level': 'DEBUG',
    		'filters': ['require_debug_true'], # 只有在Django debug为True时才在屏幕打印日志
    		'class': 'logging.StreamHandler',
    		'formatter': 'simple'
    	},
    # 默认的
        'default': {
            'level': 'INFO',
        	'class': 'logging.handlers.RotatingFileHandler', # 保存到文件，自动切
        	'filename': os.path.join(BASE_LOG_DIR, "xxx_info.log"), # 日志文件
        	'maxBytes': 1024 * 1024 * 50, # 日志大小 50M
        	'backupCount': 3, # 最多备份几个
        	'formatter': 'standard',
        	'encoding': 'utf-8',
        },
        # 专门用来记错误日志
        'error': {
        	'level': 'ERROR',
        	'class': 'logging.handlers.RotatingFileHandler', # 保存到文件，自动切
        	'filename': os.path.join(BASE_LOG_DIR, "xxx_err.log"), # 日志文件
        	'maxBytes': 1024 * 1024 * 50, # 日志大小 50M
        	'backupCount': 5,
        	'formatter': 'standard',
        	'encoding': 'utf-8',
        },
        # 专门定义一个收集特定信息的日志
        'collect': {
        	'level': 'INFO',
        	'class': 'logging.handlers.RotatingFileHandler', # 保存到文件，自动切
        	'filename': os.path.join(BASE_LOG_DIR, "xxx_collect.log"),
        	'maxBytes': 1024 * 1024 * 50, # 日志大小 50M
        	'backupCount': 5,
        	'formatter': 'collect',
        	'encoding': "utf-8"
        }
    },
    'loggers': {
        # 默认的logger应用如下配置
        '': {
        	'handlers': ['default', 'error'], # 上线之后可以把'console'移除
        	'level': 'DEBUG',
        	'propagate': True, # 向不向更高级别的logger传递
        },
        # 名为 'collect'的logger还单独处理
        'collect': {
        	'handlers': ['console', 'collect'],
        	'level': 'INFO',
        }
    },
}


import time

cur_path = os.path.dirname(os.path.realpath(__file__))  # log_path是存放日志的路径
log_path = os.path.join(os.path.dirname(cur_path), 'logs')
if not os.path.exists(log_path): os.mkdir(log_path)  # 如果不存在这个logs文件夹，就自动创建一个

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        # 日志格式
        'standard': {
            'format': '[%(asctime)s] [%(filename)s:%(lineno)d] [%(module)s:%(funcName)s] '
                      '[%(levelname)s]- %(message)s'},
        'simple': {  # 简单格式
            'format': '%(levelname)s %(message)s'
        },
    },
    # 过滤
    'filters': {
    },
    # 定义具体处理日志的方式
    'handlers': {
        # 默认记录所有日志
        'default': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(log_path, 'all-{}.log'.format(time.strftime('%Y-%m-%d'))),
            'maxBytes': 1024 * 1024 * 5,  # 文件大小
            'backupCount': 5,  # 备份数
            'formatter': 'standard',  # 输出格式
            'encoding': 'utf-8',  # 设置默认编码，否则打印出来汉字乱码
        },
        # 输出错误日志
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(log_path, 'error-{}.log'.format(time.strftime('%Y-%m-%d'))),
            'maxBytes': 1024 * 1024 * 5,  # 文件大小
            'backupCount': 5,  # 备份数
            'formatter': 'standard',  # 输出格式
            'encoding': 'utf-8',  # 设置默认编码
        },
        # 控制台输出
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        # 输出info日志
        'info': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(log_path, 'info-{}.log'.format(time.strftime('%Y-%m-%d'))),
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'standard',
            'encoding': 'utf-8',  # 设置默认编码
        },
    },
    # 配置用哪几种 handlers 来处理日志
    'loggers': {
        # 类型 为 django 处理所有类型的日志， 默认调用
        'django': {
            'handlers': ['default', 'console'],
            'level': 'INFO',
            'propagate': False
        },
        # log 调用时需要当作参数传入
        'log': {
            'handlers': ['error', 'info', 'console', 'default'],
            'level': 'INFO',
            'propagate': True
        },
    }
}