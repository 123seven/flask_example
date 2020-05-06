# @Time    : 2020-04-28 17:50
# @Author  : Seven
# @File    : example.py
# @Desc    : 示例
from flask import request
from flask_restful import Resource, reqparse

from app.libs import response


class Example(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser(bundle_errors=True)
        self.parser.add_argument('parameter', type=str, required=True, help='缺少该参数')

    def get(self):
        """
        示例
        ---
        tags:
          - 示例
        parameters:
          - name: parameter
            in: path
            type: string
            required: true
            description: 测试参数
        responses:
          200:
            description: This is an example, Work!
        """
        self.parser.parse_args()
        data = request.data
        data = {'parameter': "200"}
        return response(data)
