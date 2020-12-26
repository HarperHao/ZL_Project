"""
Author   : HarperHao
TIME    ： 2020/11/11
FUNCTION:  公共部分
"""

from flask import Blueprint, request
from utils import restful
from utils.captcha import Captcha

bp = Blueprint("common", __name__, url_prefix='/c')


@bp.route('/sms_captcha/')
def sms_captcha():
    telephone = request.args.get('telephone')
    if not telephone:
        return restful.params_error(message='请传入手机号码！')
    captcha = Captcha.gene_text(number=4)
    # 发送短信成功
    # 发送失败
