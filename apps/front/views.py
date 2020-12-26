"""
Author   : HarperHao
TIME    ： 2020/11/11
FUNCTION:  前台
"""
from io import BytesIO

from flask import Blueprint, render_template, url_for, views, make_response
from utils.captcha import Captcha

bp = Blueprint("front", __name__)


@bp.route('/')
def index():
    return render_template('front/front_index.html')


# 前台登录界面
class SignupView(views.MethodView):
    def get(self):
        return render_template('front/front_signup.html')

    def post(self):
        pass


bp.add_url_rule('/signup/', view_func=SignupView.as_view('signup'))


# 验证码图片
@bp.route('/captcha/')
def graph_captcha():
    text, image = Captcha.gene_graph_capthca()
    out = BytesIO()
    image.save(out, 'png')
    # 将指针移动到开头
    out.seek(0)
    resp = make_response(out.read())
    resp.content_type = 'image/png'
    return resp
