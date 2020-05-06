# @Time    : 2020-04-29 00:00
# @Author  : Seven
# @File    : errors.py
# @Desc    : 错误定义


from flask_restful import abort

from app.config.settings.base import RESP_SUCCESS, RESP_SUCCESS_MSG, RESP_PARAM_ERR, RESP_PARAM_ERR_MSG, \
    RESP_SERVER_ERR, \
    RESP_SERVER_ERR_MSG


def response(data=None, err=None, kwargs: dict = None):
    """
    基础 response data
    :param data: 成功返回数据
    :param err: 错误信息
    :param kwargs: 需要更新到返回内容的k v 键值对
    :return: response_data dict
    """
    response_data = {'retCode': RESP_SUCCESS, 'retMsg': RESP_SUCCESS_MSG}
    if data is not None:
        response_data['data'] = data
    if err is not None:
        response_data['error'] = err
    if kwargs:
        response_data.update(kwargs)
    return response_data


def server_error_response(err=None):
    """
    服务器错误 response data
    :param err: 错误信息
    """
    return response(err=err, kwargs={'retCode': RESP_SERVER_ERR, 'retMsg': RESP_SERVER_ERR_MSG})


def parameter_error_response(err=None):
    """
    参数错误 response data
    :param err: 错误信息
    """
    return response(err=err, kwargs={'retCode': RESP_PARAM_ERR, 'retMsg': RESP_PARAM_ERR_MSG})


def local_abort(http_status_code, *args, **kwargs):
    if http_status_code == 400:
        # 重定义400返回参数
        abort(400, **parameter_error_response(err=[kwargs.get('message')]))
    if http_status_code == 500:
        # 重定义500返回参数
        abort(500, **server_error_response(err=[kwargs.get('message')]))

    abort(http_status_code)
