from environs import Env

env = Env()

ENV = env.str('FLASK_ENV', default='production')
DEBUG = ENV == 'development'
SECRET_KEY = env.str('SECRET_KEY')
BCRYPT_LOG_ROUNDS = env.int('BCRYPT_LOG_ROUNDS', default=13)

PIPENV_IGNORE_VIRTUALENVS=1

ERROR_CODES = [400, 401, 403, 404, 405, 500, 502]

MYSQL_HOST = env.str('MYSQL_HOST', default='127.0.0.1')
MYSQL_PORT = env.int('MYSQL_PORT', default=3306)
MYSQL_DATABASE = env.str('MYSQL_DATABASE', default='cmdb')
MYSQL_USER = env.str('MYSQL_USER', default='cmdb')
MYSQL_PASSWORD = env.str('MYSQL_PASSWORD', default='123456')

# # database
SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@' \
                          f'{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}?charset=utf8'
SQLALCHEMY_BINDS = {
    'user': SQLALCHEMY_DATABASE_URI
}
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ENGINE_OPTIONS = {
    'pool_recycle': 300,
}

# # cache
CACHE_TYPE = 'redis'
CACHE_REDIS_HOST = env.str('CACHE_REDIS_HOST', default='redis')
CACHE_REDIS_PORT = env.str('CACHE_REDIS_PORT', default='6379')
CACHE_REDIS_DB = env.int('CACHE_REDIS_DB', default=9)
CACHE_REDIS_PASSWORD = env.str('CACHE_REDIS_PASSWORD', default='')
CACHE_KEY_PREFIX = 'CMDB::'
CACHE_DEFAULT_TIMEOUT = 3000

# # log
LOG_PATH = './logs/app.log'
LOG_LEVEL = 'DEBUG'

