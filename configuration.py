# 데이터베이스 접속 비밀번호
DB_PASSWORD = ''
HOST = ''
USER = ''

SECRET_KEY = ''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # engine: mysql
        'NAME' : 'sys', 
        'USER' : USER, # DB User
        'PASSWORD' : DB_PASSWORD, 
        'HOST': HOST,
        'PORT': '3306', # 데이터베이스 포트
        'OPTIONS':{
            'init_command' : "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}
