"""
Author   : HarperHao
TIME    ： 2020/12/7
FUNCTION:  扩展对象
"""
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CsrfProtect

db = SQLAlchemy()
csrf = CsrfProtect()
