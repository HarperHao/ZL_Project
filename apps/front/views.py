"""
Author   : HarperHao
TIME    ： 2020/11/11
FUNCTION:  前端
"""
from flask import Blueprint

bp = Blueprint("front", __name__)


@bp.route('/')
def index():
    return 'front index'

