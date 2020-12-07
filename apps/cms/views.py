"""
Author   : HarperHao
TIME    ： 2020/11/11
FUNCTION:  后台
"""

from flask import Blueprint, views, render_template

bp = Blueprint("cms", __name__, url_prefix='/cms')


@bp.route('/')
def index():
    return 'cms index'


# 类视图函数
class LoginView(views.MethodView):

    def get(self):
        return render_template('cms/cms_login.html')

    def post(self):
        pass


# as.view(给view_function起个名字) url_for('login')->/login/
bp.add_url_rule('/login/', view_func=LoginView.as_view('login'))
