"""
Author   : HarperHao
TIME    ： 2020/12/8
FUNCTION:  用户登录认证功能
"""
from flask import session, redirect, url_for
from functools import wraps
import config


def login_required(func):
    @wraps(func)
    def inner(*args, **kwargs):
        if config.CMS_USER_ID in session:
            print('验证cms用户')
            return func(*args, **kwargs)
        else:
            return redirect(url_for('cms.login'))

    return inner


"""
@login_required
def index():
    print('test')
    
index相当于 login_required(index)->因为login_required()会返回内层函数，所以->inner
所以index()相当于inner()
"""
