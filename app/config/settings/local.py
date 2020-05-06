# @Time    : 2020-05-06 13:30
# @Author  : Seven
# @File    : local.py
# @Desc    : 本地配置

from .base import *

# 数据库连接配置
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:12345@127.0.0.1:3306/ginger?charset=utf8'
SQLALCHEMY_POOL_SIZE = 5
SQLALCHEMY_POOL_TIMEOUT = 10
SQLALCHEMY_TRACK_MODIFICATIONS = False

DEBUG = True
