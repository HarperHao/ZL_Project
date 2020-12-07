"""
Author   : HarperHao
TIME    ： 2020/11/11
FUNCTION:  公共部分
"""

from flask import Blueprint

bp = Blueprint("common", __name__, url_prefix='/common')


@bp.route('/')
def index():
    return 'common index'
