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
        """获取用户信息123.
        ---
            tags: 
              - Greeting API
            parameters:
              - name: _id
                in: path
                description: 用户ID
              - name: name
                description: 用户名称
              - name: type
                description: 用户类型（1/2/3）
              - name: startTime
                description: 开始时间
              - name: endTime
                description: 结束时间
            responses: 
              200: 
                description: 返回查询成功
      
              
        """
        # print(f"查询id为{_id}用户成功...")
        # return self.jsonify(_id)
        params = request.args
        name = params.get('name', 'World')
        print(f"查询id为{_id}用户成功..., 参数ID为{_id}")
        return self.jsonify({"message": f"Hello, {params}!"})

    def put(self, _id):
        """更新用户信息."
        ---
            tags:
              - Greeting API
            parameters:
              - name: name
        """
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
