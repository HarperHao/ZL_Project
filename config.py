"""
Author   : HarperHao
TIME    ： 2020/12/7
FUNCTION:
12/7 ->导入数据库配置文件
12/8 ->设置session的key和时间、secret_key
"""
from datetime import timedelta

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
# 设置cookie过期时间
PERMANENT_SESSION_LIFETIME = timedelta(days=1)
# 设置session的key
CMS_USER_ID = 'Hao'
# 给session设置secret_key
SECRET_KEY = 'Hao'

# 配置邮件
# 发信服务器
MAIL_SERVER = "smtp.qq.com"
MAIL_PORT = '587'
MAIL_USE_TLS = True
# MAIL_USE_SSL
# 发信服务器的邮箱地址
MAIL_USERNAME = "1310160680@qq.com"
# 授权码
MAIL_PASSWORD = "afvldorrfkwygjee"

#默认的发信人
MAIL_DEFAULT_SENDER = "1310160680@qq.com"
