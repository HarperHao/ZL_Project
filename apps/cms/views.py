"""
Author   : HarperHao
TIME    ： 2020/11/11
FUNCTION:  后台
2020/12/7->类视图函数
12/8->表单验证、session使用
"""

from flask import Blueprint, views, render_template, request, redirect, url_for, session
from .forms import LoginForm
from .models import CMSUser
import config
from .decorators import login_required

bp = Blueprint("cms", __name__, url_prefix='/cms')


@bp.route('/')
@login_required
def index():
    return render_template('cms/cms_index.html')


# 类视图函数
class LoginView(views.MethodView):

    def get(self, message=None):
        return render_template('cms/cms_login.html', message=message)

    # apps / cms /.views.py
    def post(self):
        form = LoginForm(request.form)
        # 输入无误
        if form.validate():
            email = form.email.data
            password = form.password.data
            remember = form.remember.data
            user = CMSUser.query.filter_by(email=email).first()

            if user and user.check_password(password):
                print('登录成功')
                session[config.CMS_USER_ID] = user.id
                if remember:
                    session.permanent = True
                return redirect(url_for('cms.index'))
            # 用户的邮箱和密码与数据库中的不匹配
            else:
                return self.get(message='邮箱或密码错误')
        # 失败的话提示错误信息，并重定向到登录页面
        else:
            message = form.errors.popitem()
            print(message)
            return self.get(message=message[1][0])


# as.view(给view_function起个名字) url_for('login')->/login/
bp.add_url_rule('/login/', view_func=LoginView.as_view('login'))
