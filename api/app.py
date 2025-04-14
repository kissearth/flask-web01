
from flask import Flask, Blueprint
from inspect import getmembers

from api.extensions import db
from api.extensions import swagger

import api.views.entry

def create_app(config_object="settings"): 
    app = Flask(__name__.split(".")[0])

    app.config.from_object(config_object)

    register_extensions(app)
    register_blueprints(app)

    return app

def register_blueprints(app: Flask):
    for item in getmembers(api.views.entry):
        # print(f'类型是: {type(item)}, 结果是：{item}')
        if item[0].startswith("blueprint") and isinstance(item[1], Blueprint):
            print(f"找到蓝图：名称:{item[0]} ==> 值为：{item[1]}")
            app.register_blueprint(item[1])
    print(f'存在的url：{app.url_map}')
            

def register_extensions(app): 
    """Register Flask extensions."""

    # db.init_app(app)
    swagger.init_app(app)


