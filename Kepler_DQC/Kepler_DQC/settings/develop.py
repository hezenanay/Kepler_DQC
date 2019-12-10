from .base import * # NOQA

DEBUG = True

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', #数据库引擎
        'NAME': 'test',                       #数据库名
        'USER': 'root',                       #用户名
        'PASSWORD': 'HZN60213991d',           #密码
        'HOST': '',                           #数据库主机，默认为localhost
        'PORT': '',                           #数据库端口，MySQL默认为3306
        'OPTIONS': {
            'autocommit': True,
         },
    }
}