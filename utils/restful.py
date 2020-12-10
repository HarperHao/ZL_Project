"""
Author   : HarperHao
TIME    ： 2020/12/10
FUNCTION:  返回的json数据规范
"""
from flask import jsonify


class HttpCode:
    ok = 200
    unauth_error = 401
    params_error = 400
    server_error = 500


def restful_result(code, message, data):
    return jsonify({'code': code,
                    'message': message,
                    'data': data
                    })


def success(message='Success', data=None):
    return restful_result(HttpCode.ok, message=message, data=data)


def unauth_error(message='用户没有被授权'):
    return restful_result(HttpCode.unauth_error, message=message, data=None)


def params_error(message='参数错误'):
    return restful_result(HttpCode.params_error, message=message, data=None)


def server_error(message='服务器内部错误'):
    return restful_result(HttpCode.server_error, message=message, data=None)
