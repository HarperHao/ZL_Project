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

    # 判断用户有多少权限
    @property
    def permissions(self):
        if not self.roles:
            return 0
        else:
            all_permissions = 0
            for role in self.roles:
                all_permissions = role.permissions | all_permissions
            return all_permissions

    # 判断用户是否拥有某一权限
    def has_permission(self, permission):
        return permission & self.permissions

    # 判断用户是否为开发人员
    @property
    def is_developer(self):
        return self.has_permission(CMSPermission.ALL_PERMISSION)


# 权限模型
class CMSPermission(object):
    # 用二进制来表示权限
    # 所有权限
    ALL_PERMISSION = 0b11111111
    # 1. 访问者权限
    VISITOR = 0b00000001
    # 2. 管理帖子权限
    POSTER = 0b00000010
    # 3. 管理评论的权限
    COMMENTER = 0b00000100
    # 4. 管理板块的权限
    BOARDER = 0b00001000
    # 5. 管理前台用户的权限
    FRONTUSER = 0b00010000
    # 6. 管理后台用户的权限
    CMSUSER = 0b00100000
    # 7. 管理后台管理员的权限
    ADMINER = 0b01000000


# 角色与用户之间是多对多关系，建立关联表
cms_role_user = db.Table(
    'cms_role_user',
    db.Column('cms_role_id', db.Integer, db.ForeignKey('cms_role.id'), primary_key=True),
    db.Column('cms_user_id', db.Integer, db.ForeignKey('cms_user.id'), primary_key=True)
)


# 角色模型
class CMSRole(db.Model):
    __tablename__ = 'cms_role'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    desc = db.Column(db.String(200), nullable=True)
    create_time = db.Column(db.DateTime, default=datetime.now)
    permissions = db.Column(db.Integer, default=CMSPermission.VISITOR)

    users = db.relationship('CMSUser', secondary=cms_role_user, backref='roles')
