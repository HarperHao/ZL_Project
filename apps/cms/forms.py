"""
Author   : HarperHao
TIME    ： 2020/12/8
FUNCTION:  表单验证器
"""
from flask import g
from wtforms import StringField, IntegerField, ValidationError
from wtforms.validators import Email, Length, InputRequired, EqualTo
from ..forms import BaseForm
from utils import zlcache


class LoginForm(BaseForm):
    email = StringField(validators=[Email(message='请输入正确格式的邮箱'), InputRequired('请输入邮箱！')])
    password = StringField(validators=[Length(min=4, max=20, message='密码的长度必须在4位到20位之间'), InputRequired("请输入密码！")])
    remember = IntegerField()


class RestpwdForm(BaseForm):
    oldpwd = StringField(validators=[Length(min=4, max=20, message='请输入正确格式的旧密码')])
    newpwd = StringField(validators=[Length(min=4, max=20, message='请输入正确格式的新密码')])
    newpwd2 = StringField(validators=[EqualTo("newpwd", message='两次输入的密码必须一致')])


class ResetEmailForm(BaseForm):
    email = StringField(validators=[Email(message='请输入正确格式的邮箱')])
    captcha = StringField(validators=[Length(min=6, max=6, message='请输入正确长度的验证码')])

    # 确保新的邮箱和原来的邮箱不是同一个邮箱
    def validate_email(self, field):
        # 新的邮箱
        email = field.data
        user = g.cms_user
        if email == user.email:
            raise ValidationError("不能修改为同一个邮箱")

    # 验证输入的验证码和邮箱发送的验证码是否一致
    def validate_captcha(self, field):
        # 输入的验证码
        captcha = field.data
        # 获取邮箱发送的验证码
        email = self.email.data
        captcha_cache = zlcache.get(email)
        if not captcha_cache or captcha.lower() != captcha_cache.lower():
            raise ValidationError('邮箱验证码输入错误！')
