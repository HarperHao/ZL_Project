"""
Author   : HarperHao
TIME    ： 2020/12/8
FUNCTION:  表单验证器，对管理员的信息进行验证
"""

from wtforms import Form,StringField, IntegerField
from wtforms.validators import Email, Length, InputRequired, EqualTo
from ..forms import BaseForm


class LoginForm(Form):
    email = StringField(validators=[Email(message='请输入正确格式的邮箱'), InputRequired('请输入邮箱！')])
    password = StringField(validators=[Length(min=4, max=20, message='密码的长度必须在4位到20位之间'), InputRequired("请输入密码！")])
    remember = IntegerField()


class RestpwdForm(Form):
    oldpwd = StringField(validators=[Length(min=4, max=20, message='请输入正确格式的旧密码')])
    newpwd = StringField(validators=[Length(min=4, max=20, message='请输入正确格式的新密码')])
    newpwd2 = StringField(validators=[EqualTo("newpwd", message='两次输入的密码必须一致')])
