"""
Author   : HarperHao
TIME    ： 2020/12/7
FUNCTION:
12/7 ->导入数据库配置文件
"""
DEBUG = True
DB_USERNAME = 'root'
DB_PASSWORD = 'root'
DB_HOST = '127.0.0.1'
DB_PORT = '3306'
DB_NAME = 'zlbbs'

# PERMANENT_SESSION_LIFETIME =

DB_URI = 'mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8' % (DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
