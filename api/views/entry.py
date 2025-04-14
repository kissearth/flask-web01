from flask import Blueprint
from flask_restful import Api

from api.views.test_api import TestApiGetAddView, TestApiUpdateDelView, TestApiCITypeView

blueprint_test = Blueprint("test_api", __name__, url_prefix="/api/test")
test_api_rest = Api(blueprint_test)
test_api_rest.add_resource(TestApiGetAddView, *TestApiGetAddView.url_prefix)
test_api_rest.add_resource(TestApiUpdateDelView, *TestApiUpdateDelView.url_prefix)
test_api_rest.add_resource(TestApiCITypeView, *TestApiCITypeView.url_prefix)

