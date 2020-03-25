from .base import *
import platform

DEBUG = True

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

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

STATICFILES_DIRS = [
    # 실제 static 파일은 모두 client 측에서 소유 
    os.path.join(PROJECT_ROOT, 'client/static')
]

print("[gomja] project root : ", PROJECT_ROOT)
print("[gomja] static root : ", STATIC_ROOT)

LOGIN_REDIRECT_URL = 'http://127.0.0.1:3000'
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_EMAIL_CONFIRMATION_HMAC =True
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 300

SOCIALACCOUNT_AUTO_SIGNUP = False

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = os.path.join(PROJECT_ROOT, 'tmp/email')