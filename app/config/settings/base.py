# @Time    : 2020-04-28 17:05
# @Author  : Seven
# @File    : base.py
# @Desc    : 通用配置项


# swagger 配置
# 配置标题
SWAGGER_TITLE = 'ginger'
# 配置公共描述内容
SWAGGER_DESC = 'ginger API'
# 配置文档URL路径
SWAGGER_ROUTE = '/docs/'
# 项目版本
SWAGGER_VERSION = '0.1'

# response error 配置
# 成功
RESP_SUCCESS = 200
RESP_SUCCESS_MSG = '成功 | Success'
# 参数错误
RESP_PARAM_ERR = 400
RESP_PARAM_ERR_MSG = '参数错误 | Fail'
# 服务器错误
RESP_SERVER_ERR = 500
RESP_SERVER_ERR_MSG = '服务器错误 | Fail'

# 数据库配置
# 数据库连接配置
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@127.0.0.1:3306/ginger?charset=utf8'
# 配置 SQLAlchemy 的连接池大小
SQLALCHEMY_POOL_SIZE = 5
# 配置 SQLAlchemy 的连接超时时间
SQLALCHEMY_POOL_TIMEOUT = 15
# 跟踪对象的修改，在本例中用不到调高运行效率，所以设置为False
SQLALCHEMY_TRACK_MODIFICATIONS = False

DEBUG = True