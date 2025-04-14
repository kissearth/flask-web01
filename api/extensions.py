from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger

db = SQLAlchemy(session_options={"autoflush": False})
swagger = Swagger(template={
    "swagger": "2.0",
    "info": {
        "title": "管理系统API文档",
        "description": "提供用户管理、权限管理等后台管理系统各类API接口", 
        "version": "1.0.0",
        "contact": {
            "name": "管理员",
            "email": "admin@example.com",
            "url": "https://www.baidu.com"
        },
        "license": {
            "name": "Apache 2.0",
            "url": "http://www.apache.org/licenses/LICENSE-2.0.html"
        }
    },
    "host": "localhost:5000",
    "basePath": "/api",
    "schemes": ["http", "https"]
})

