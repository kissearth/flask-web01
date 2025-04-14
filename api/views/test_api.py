# -*- coding:utf-8 -*-

from flask import request
from werkzeug.datastructures import MultiDict

from api.resource import APIView

prefix = "/tests"

class TestApiGetAddView(APIView):

    url_prefix = (f'{prefix}/list',)

    def get(self):
        params = request.args
        params_keys = params.keys()
        params_values = params.values()
        print(f"数据列表查询成功..., 参数key列表: {params}，key类型：{type(params_keys)}, 值类型: {type(params_values)}")
        return self.jsonify("123456")

    def post():
        json_data = request.json
        multi_dict_data = MultiDict(json_data)
        print('数据保存成功...')


class TestApiUpdateDelView(APIView):
    """ 更新和删除 """

    url_prefix = (f'{prefix}/<int:_id>',)

    def get(self, _id):
        print(f"查询id为{_id}用户成功...")
        return self.jsonify(_id)

    def put(self, _id):
        json_data = request.json
        multi_dict_data = MultiDict(json_data)
        print('数据更新成功...')

    def delete(self, _id):
        params = request.args
        print(f"收到更新参数：{_id}")
        return self.jsonify(_id)

from api.models.ci_type import CIType

class TestApiCITypeView(APIView):
     
    url_prefix = (f'{prefix}/types',)
    
    def get(self):
        types = CIType.query.all()
        print("获取的结果如下：")
        for type in types:
            print(f"结果是： {type}")
        return self.jsonify(len(types)), 200
