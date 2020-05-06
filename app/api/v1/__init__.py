# @Time    : 2020-04-28 17:16
# @Author  : Seven
# @File    : __init__.py.py
# @Desc    : 版本

from flask import Blueprint
from flask_restful import Api

from app.api.v1 import example


def register_views(blueprint):
    """
    注册 Restful Api 到 Blueprint
    :param blueprint: Blueprint v1
    """
    api = Api(blueprint)
    api.add_resource(example.Example, '/example')


def create_blueprint_v1():
    """
    创建 Blueprint
    :return: Blueprint v1
    """
    v1 = Blueprint('v1', __name__)
    register_views(v1)
    return v1
