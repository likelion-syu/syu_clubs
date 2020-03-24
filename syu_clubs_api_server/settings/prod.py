from .base import *
import platform

DEBUG = False

ALLOWED_HOSTS = ['*']


platform = platform.platform()
if platform == "Linux-4.19.76-linuxkit-x86_64-with-glibc2.2.5":
    DATABASES = { 
        'default' : {
            'ENGINE' : 'django.db.backends.mysql',
            'HOST' : '10.10.0.2',
            'OPTIONS' : {
                'read_default_file' : os.path.join(PROJECT_ROOT, './secure/mysql.cnf'),
                'init_command' : "SET sql_mode='STRICT_TRANS_TABLES'",
            }
        }
    }
else :
    DATABASES = { 
        'default' : {
            'ENGINE' : 'django.db.backends.mysql',
            'HOST' : '127.0.0.1',
            'OPTIONS' : {
                'read_default_file' : os.path.join(PROJECT_ROOT, './secure/mysql.cnf'),
                'init_command' : "SET sql_mode='STRICT_TRANS_TABLES'",
            }
        }
    }


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, "static")

STATICFILES_DIRS = [
    # 실제 static 파일은 모두 client 측에서 소유 
    os.path.join(PROJECT_ROOT, 'client/static')
]


STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'