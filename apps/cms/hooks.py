"""
Author   : HarperHao
TIME    ： 2020/12/9
FUNCTION:  钩子函数
"""
from flask import session, g
from .views import bp
from .models import CMSUser, CMSPermission
import config


@bp.before_request
def before_request():
    if config.CMS_USER_ID in session:
        user_id = session.get(config.CMS_USER_ID)
        user = CMSUser.query.get(user_id)
        print('user:{}'.format(user.username))
        if user:
            g.cms_user = user


@bp.context_processor
def cms_context_processor():
    return {"CMSPermission": CMSPermission}
