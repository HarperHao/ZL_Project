"""
Author   : HarperHao
TIME    ： 2020/12/7
FUNCTION:  创建用户模型
#难点1：给密码进行加密的方法二的理解，两个构造器的用法和创建数据库中插入的一条记录的过程更加清楚
"""
from exts import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class CMSUser(db.Model):
    __tablename__ = 'cms_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), nullable=False)
    # 将password设置为私有变量
    _password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    join_time = db.Column(db.DateTime, default=datetime.now)

    # 方法一
    # def __init__(self, username, raw_password, email):
    #     self.username = username
    #     self._password = generate_password_hash(raw_password)
    #     self.email = email

    # 方法二

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    @property
    def password(self):
        raise AttributeError('password 是不可读属性')
        # return self._password

    @password.setter
    def password(self, raw_password):
        self._password = generate_password_hash(raw_password)

    def check_password(self, raw_password):
        result = check_password_hash(self._password, raw_password)
        return result
