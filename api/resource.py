# -*- coding:utf-8 -*-

from flask import jsonify, send_file
from flask_restful import Resource


class APIView(Resource):

    def __init__(self):
        super(APIView, self).__init__()

    @staticmethod
    def jsonify(*args, **kvargs):
        return jsonify(*args, **kvargs)

    def send_file(*args, **kwargs):
        return send_file(*args, **kwargs)
    

def register_blueprint_resources():
    """ 注册所有蓝图资源 """
    pass
