import inspect

class MyClass:

    from flask import Blueprint
    from flask_restful import Api

    x = 10

    def __init__(self, y):
        self.y = y

    def my_method(self):
        pass

members = inspect.getmembers(MyClass)
for name, value in members:
    print(f"{name}: {value}")
