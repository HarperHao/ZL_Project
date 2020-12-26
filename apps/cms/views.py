"""
Author   : HarperHao
TIME    ： 2020/11/11
FUNCTION:  后台
2020/12/7->类视图函数
12/8->表单验证、session使用
"""

from flask import Blueprint, views, render_template, request, redirect, url_for, session, g
from flask_mail import Message
import string
import random
from .forms import LoginForm, RestpwdForm, ResetEmailForm
from .models import CMSUser, CMSPermission
from exts import db, mail
import config
from .decorators import login_required, permission_required
from utils import restful, zlcache

bp = Blueprint("cms", __name__, url_prefix='/cms')


# 登录后的主页面
@bp.route('/')
@login_required
def index():
    #print('用户的密码是{}'.format(g.cms_user.password))
    return render_template('cms/cms_index.html')


# 注销
@bp.route('/logout/')
@login_required
def logout():
    del session[config.CMS_USER_ID]
    return redirect(url_for('cms.login'))


# 个人信息视图
@bp.route('/profile/')
@login_required
def profile():
    print('个人信息视图')
    return render_template('cms/cms_profile.html')


# 登录类视图函数
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


# 修改密码类视图函数
class ResetPwdView(views.MethodView):
    decorators = [login_required]

    def get(self):
        return render_template('cms/cms_resetpwd.html')

    def post(self):

        form = RestpwdForm(request.form)
        if form.validate():
            user = g.cms_user
            oldpwd = form.oldpwd.data
            newpwd = form.newpwd.data
            if user.check_password(oldpwd):
                user.password = newpwd
                db.session.commit()
                return restful.success()
            else:
                return restful.params_error(message='旧密码错误')
        else:
            message = form.get_error()
            return restful.params_error(message=message)


bp.add_url_rule('/resetpwd/', view_func=ResetPwdView.as_view('resetpwd'))


# 修改邮箱视图类
class ResetEmailView(views.MethodView):
    decorators = [login_required]

    def get(self):
        return render_template('cms/cms_resetemail.html')

    def post(self):
        print('进入post')
        form = ResetEmailForm(request.form)
        if form.validate():
            print('邮箱验证成功')
            email = form.email.data
            g.cms_user.email = email
            db.session.commit()
            return restful.success()
        else:
            print('邮箱验证失败')
            return restful.params_error(form.get_error())


bp.add_url_rule('/resetemail/', view_func=ResetEmailView.as_view('resetemail'))


# @bp.route('/email/')
# @login_required
# def sendEmail_test():
#     message = Message(subject='这是一封测试邮件', recipients=['1310160680@qq.com', '1150475496@qq.com'], body='你好，这是一封测试邮件')
#     mail.send(message)
#     return 'success'

@bp.route('/email_captcha/')
def email_captcha():
    # 从url中获取参数
    email = request.args.get('email')
    if not email:
        return restful.params_error('请输入邮箱')
    # 生成验证码
    source_letters = string.ascii_letters + string.digits
    # temp是一个列表
    temp = random.sample(source_letters, 6)
    captcha = ''.join(temp)
    # print(temp)
    print('邮箱验证码为:{}'.format(''.join(temp)))

    # 给邮箱发送邮件
    message = Message(subject='Python论坛邮箱验证码', recipients=[email], body='您的验证码是：{}'.format(captcha))
    try:
        mail.send(message)
    except:
        return restful.server_error()
    zlcache.set(email, captcha)
    return restful.success()


@bp.route('/posts/')
@login_required
@permission_required(CMSPermission.POSTER)
def posts():
    return render_template('cms/cms_posts.html')


@bp.route('/comments/')
@login_required
@permission_required(CMSPermission.COMMENTER)
def comments():
    return render_template('cms/cms_comments.html')


@bp.route('/boards/')
@login_required
@permission_required(CMSPermission.BOARDER)
def boards():
    return render_template('cms/cms_boards.html')


@bp.route('/fusers/')
@login_required
@permission_required(CMSPermission.FRONTUSER)
def fusers():
    return render_template('cms/cms_fusers.html')


@bp.route('/cusers/')
@login_required
@permission_required(CMSPermission.CMSUSER)
def cusers():
    return render_template('cms/cms_cusers.html')


@bp.route('/croles/')
@login_required
@permission_required(CMSPermission.ALL_PERMISSION)
def croles():
    return render_template('cms/cms_croles.html')
