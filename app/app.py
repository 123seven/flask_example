# @Time    : 2020-04-28 17:01
# @Author  : Seven
# @File    : __init__.py.py
# @Desc    : Flask初始化

import logging
import os
import sys
from logging.handlers import RotatingFileHandler

import flask_restful
from flasgger import Swagger
from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix

from app.api.v1 import create_blueprint_v1
from app.config import CONFIG_NAME_MAPPER
from app.libs import abort
from app.libs.model import db
from app.libs.utils import JSONEncoder


def init_logging(app):
    """
    初始化 flask log 配置
    :param app: flask app
    """
    app.logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter("[%(asctime)s] - [%(pathname)s:%(lineno)d] - %(levelname)s - %(message)s")
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(formatter)
    app.logger.addHandler(stream_handler)
    handler = RotatingFileHandler('{}/log/ik_agent.log'.format(os.getcwd()), maxBytes=1024 * 1024 * 10, backupCount=20)
    handler.setLevel(logging.INFO)
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)


def register_blueprints(app):
    """
    注册 Blueprint
    :param app: flask app
    """
    app.register_blueprint(create_blueprint_v1(), url_prefix='/api/v1')


def init_swagger(app):
    """
    初始化 swagger，并载入配置
    :param app: flask app
    """
    swagger_config = Swagger.DEFAULT_CONFIG
    swagger_config['title'] = app.config.get('SWAGGER_TITLE')
    swagger_config['description'] = app.config.get('SWAGGER_DESC')
    swagger_config['specs_route'] = app.config.get('SWAGGER_ROUTE')
    swagger_config['version'] = app.config.get('SWAGGER_VERSION')

    Swagger(app, config=swagger_config)


def init_db(app):
    """
    载入数据库配置
    :param app: flask app
    """

    # 注册数据库连接
    db.app = app
    db.init_app(app)


def load_setting(app, flask_config_name=None):
    """
    多环境配置
    :param app:
    :param flask_config_name: 指定环境，默认读取local
    """
    app.wsgi_app = ProxyFix(app.wsgi_app)
    env_flask_config_name = os.getenv('FLASK_CONFIG')
    # 指定环境
    config_mapper_name = flask_config_name or env_flask_config_name or 'local'
    config_name = CONFIG_NAME_MAPPER[config_mapper_name]
    app.config.from_object(config_name)


def creat_app():
    """
    创建 flask app
    :return: flask app
    """
    # init flask
    app = Flask(__name__)

    # load config
    load_setting(app)

    # register blueprints
    register_blueprints(app)

    # init swagger
    init_swagger(app)

    # 返回json格式转换
    app.json_encoder = JSONEncoder

    # 自定义错误
    flask_restful.abort = abort

    # init db
    init_db(app)

    # init flask log
    init_logging(app)

    return app


__all__ = ['creat_app']
