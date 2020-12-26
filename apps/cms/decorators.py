"""
Author   : HarperHao
TIME    ： 2020/12/8
FUNCTION:  钩子函数汇聚地
"""
from flask import session, redirect, url_for, g
from functools import wraps
import config


def login_required(func):
    @wraps(func)
    def inner(*args, **kwargs):
        if config.CMS_USER_ID in session:
            # print('验证cms用户')
            return func(*args, **kwargs)
        else:
            return redirect(url_for('cms.login'))

    return inner


# 权限认证
def permission_required(permission):
    def outter(func):
        @wraps(func)
        def inner(*args, **kwargs):
            user = g.cms_user
            if user.has_permission(permission):
                return func(*args, **kwargs)
            else:
                return redirect(url_for('cms.index'))

        return inner

    return outter


"""
@login_required
def index():
    print('test')
    
index相当于 login_required(index)->因为login_required()会返回内层函数，所以->inner
所以index()相当于inner()
"""
